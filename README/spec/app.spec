############################################
#
# Possible values for apps
# 
############################################

<appname>
* Application Name (Path name)

  [apps|deployment_apps|master_apps|shcluster/apps]:
  * Installation destination
  * Note: Underscore instead of dash needed due to YAML Syntax

    install: <bool>
    * Should the app be installed.
    * Used to uninstall app

    clean_install: <bool>
    * Should the app directory be purged before (re-)installation

    bundle: <filename>
    * The file that contains the app (tar.gz/spl)
    * File must reside unter splunk_repository.repository_root/<appname>/<filename>

<appname>
...
