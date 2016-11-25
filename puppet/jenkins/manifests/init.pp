# Class: jenkins
# Description: Installs Jenkins-CI as service & creates Proxy.
# https://jenkins-ci.org/
# 
# Written by: Courtney Cotton <cotton@cottoncourtney.com> 09-20-2015
#
# Requirements
# Apache Proxy (VirtualHost configuration) for Jenkins, Hiera

class jenkins {
  
  $servername = hiera('jenkins::web::server', 'jenkins')
  $doc_root   = hiera('jenkins::web::docroot','/var/wwww/html')

  include jenkins::packages
  include jenkins::repo
  include jenkins::service
  include jenkins::proxy
}
