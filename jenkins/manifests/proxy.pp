# Class: jenkins::proxy
class jenkins::proxy {
  file {'/etc/httpd/conf.d/jenkins':
    ensure  => 'file',
    owner   => 'root',
    group   => 'root',
    mode    => '0755',
    content => template('jenkins/vhost.erb'),
  }
}
