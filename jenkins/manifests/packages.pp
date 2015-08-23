# Class: jenkins::packages
# Description: Installs Jenkins + Dependencies
class jenkins::packages {
  $rpackages = [ 'java-1.7.0-openjdk', 'jenkins' ]
  package { $rpackages:
    ensure  => latest,
    require => Yumrepo['jenkins'],
  }
}
