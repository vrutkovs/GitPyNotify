#!/usr/bin/env python

from git import *
from gi.repository import Notify
repo = Repo("~/Devel/IRR")
origin = repo.remotes.origin

current_master_HEAD_commit_sha = repo.head.commit.hexsha
origin_master_HEAD_commit_sha = origin.refs[0].commit.hexsha

if current_master_HEAD_commit_sha != origin_master_HEAD_commit_sha:
    # Get details on commit
    origin_commit = origin.refs[0].commit
    title = "New commit in %s by %s" % (origin.url,
                                    origin_commit.committer.name)
    message = "%s\n\n%s" % (origin_commit.summary,
                        origin_commit.message)

    Notify.init (title)
    Hello=Notify.Notification.new (title,
                               message,
                               "dialog-information")
    Hello.show ()
