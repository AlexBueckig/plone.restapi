# -*- coding: utf-8 -*-
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.services import Service
from plone.restapi.deserializer import json_body
from zExceptions import BadRequest
from Products.CMFCore.utils import getToolByName
from Products.CMFEditions import CMFEditionsMessageFactory as _
from Products.CMFEditions.interfaces.IModifier import FileTooLargeToVersionError  # noqa


class HistoryPatch(Service):

    def reply(self):
        body = json_body(self.request)
        message = revert(self.context, body['version_id'])
        return json_compatible(message)


def revert(context, version_id):
    pr = getToolByName(context, 'portal_repository')
    pr.revert(context, version_id)

    title = context.title_or_id()
    if not isinstance(title, unicode):
        title = unicode(title, 'utf-8', 'ignore')

    if pr.supportsPolicy(context, 'version_on_revert'):
        try:
            commit_msg = context.translate(
                _(u'Reverted to revision ${version}',
                  mapping={'version': version_id})
            )
            pr.save(obj=context, comment=commit_msg)
        except FileTooLargeToVersionError:
            raise BadRequest({
                'message': u'The most current revision of the file could not '
                            'be saved before reverting because the file is '
                            'too large.'
            })

    msg = u'{} has been reverted to revision {}.'.format(title, version_id)
    return {'message': msg}
