#!/usr/bin/env python
# -*- coding: utf-8 -*-
from googl.short import GooglUrlShort
from django.conf import settings

GENERATE_SHORT_URL = getattr(settings, 'GENERATE_SHORT_URL', False)


def shorturl_generate(sender, instance, created, **kwargs):
    if GENERATE_SHORT_URL:
        if not instance.short_url:
            instance.short_url = GooglUrlShort(
                instance.get_http_absolute_url()
            ).short()
            instance.save()


def delete_container(sender, instance, using, **kwargs):
    """
    Ensure objects are deleted from mother class Article
    when deleted from child class
    """
    try:
        instance.__class__.objects.filter(
            child_class=instance.child_class,
            slug=instance.slug,
            channel=instance.channel,
            site=instance.site
        ).delete()
    except instance.__class__.DoesNotExist:
        # object not exists
        pass
