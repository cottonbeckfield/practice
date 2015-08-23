# Class; jenkins::repo
# Description: Installs the Jenkins repo
class jenkins::repo {
  yumrepo { 'jenkins':
    baseurl  => 'http://jenkins-ci.org/redhat',
    descr    => 'Jenkins RHEL Repo',
    enabled  => 1,
    gpgkey   => 'https://jenkins-ci.org/redhat/jenkins-ci.org.key',
    gpgcheck => 1,
  }
}
