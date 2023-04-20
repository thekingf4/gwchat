# -*- coding: utf-8 -*-


import setuptools

setuptools.setup(
    name="gwchat_tab",
    version="0.3",
    license="MIT",
    description="gwchat Open edX course_tab",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Platform :: Open edX",
        "Natural Language :: English",
        "Environment :: Web Environment",
    ],
    entry_points={
        "lms.djangoapp": [
            "gwchat_tab = gwchat_tab.apps:GwChatConfig",
        ],
        "openedx.course_tab": [
            "gwchat_tab = gwchat_tab.plugins:GwChatTab",
        ]
    },
)
