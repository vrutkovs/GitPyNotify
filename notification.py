#!/usr/bin/env python

from gi.repository import GObject, Notify
from git import *

class RepoNotification:
    repo = None
    last_notified_commit = None
    main_loop = GObject.MainLoop()
    
    def __init__(self, 
                 repo_path,
                 timeout=10000):
        # Initialize repo here
        self.repo = Repo (repo_path)
        self.origin = self.repo.remotes.origin
        
        self.last_notified_commit = self.__get_local_head_sha()
        
        # Check on start
        self.check_for_new_revision()
        
        # Timeout magic
        self.timeout_handler = GObject.timeout_add (timeout, 
                                                    self.check_for_new_revision) 
        self.main_loop.run() 
    
    def check_for_new_revision(self):
        origin_HEAD_sha = self.origin.refs[0].commit.hexsha
        if self.last_notified_commit != origin_HEAD_sha:
            # Get details on commit
            origin_commit = self.origin.refs[0].commit
            self.__show_notification(self.origin.url,
                                     origin_commit.committer.name,
                                     origin_commit.summary)
            self.last_notified_commit = origin_HEAD_sha
        return True

    
    def __show_notification(self, url, committer, summary):
        title = "New commit in %s by %s" % (url, committer)

        Notify.init (title)
        Hello=Notify.Notification.new (title,
                                       summary,
                                       "dialog-information")
        Hello.show ()
    
    def __get_local_head_sha(self):
        return self.repo.head.commit.hexsha

