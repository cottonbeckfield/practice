require 'spec_helper'

  describe 'jenkins' do
      it { should contain_class 'jenkins::service' }
  end 

  describe 'jenkins' do
     it { should contain_class 'jenkins::packages' }
  end
