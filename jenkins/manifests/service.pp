# Class: jenkins::service
class jenkins::service {
  service { 'jenkins':
    ensure  => running,
    enable  => true,
    require => Package['jenkins'],
  }
}
