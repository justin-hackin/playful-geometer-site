#!/bin/bash
s3cmd sync --acl-public model_browser/staticfiles/ s3://playful_geometer_site
