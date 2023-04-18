# -*- coding: utf-8 -*-


import setuptools

setuptools.setup(
    name="gwchat",
    version="0.1.",
    license="MIT",
    description="gwchat Open edX course_tab",
    # url="https://github.com/tony-h/rocketchat-tab",
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
            "bbb_tab = gwchat.apps:GraspwayChatConfig",
        ],
        "openedx.course_tab": [
            "gwchat = gwchat.plugins:GraspwayChatTab",
        ]
    },
)
