#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/images/', include('opps.images.urls')),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^fileupload/', include('opps.contrib.fileupload.urls')),

    url(r'^sitemap', include('opps.sitemaps.urls')),

    url(r'^api/', include('opps.api.urls', namespace='api',
                          app_name='api')),

    url(r'^', include('opps.flatpages.urls', namespace='flatpages',
                      app_name='flatpages')),

    url(r'^', include('opps.articles.urls', namespace='articles',
                      app_name='articles')),

    url(r'^', include('opps.containers.urls', namespace='containers',
                      app_name='containers')),
)
