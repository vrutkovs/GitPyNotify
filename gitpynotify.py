#!/usr/bin/env python

from optparse import OptionParser
import json
from gi.repository import Gio

def load_configuration():
    # Load configuration from dconf
    settings = Gio.Settings.new("com.github.roignac.gitpynotify")
    return json.loads(settings.get_string("configuration"))

def run_as_daemon(configuration):
    # Parse configuration
    repo_object_collection = []
    for repo in configuration['repos']:
        dummy = RepoNotification(repo['path'], repo['timeout'])
        repo_object_collection.append(dummy)

if __name__=="__main__":
    parser = OptionParser()
    parser.add_option("-c", "--configure", help="configure settings")

    (options, args) = parser.parse_args()
    
    configuration = load_configuration()
    
    if options['configure'] or configuration == None:
        # Show GUI here
        print "Here be GUI"
    else:
        run_as_daemon(configuration)
