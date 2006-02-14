# TODO:
# - small binary to run ;)
Summary:	Plotting library written in ruby
Summary(pl):	Biblioteka do rysowania w rubym
Name:		mrplot
Version:	0.0.1
Release:	0.1
License:	MIT/X Consortium License
Group:		Applications/Graphics
Source0:	http://rubyforge.org/frs/download.php/2884/%{name}-%{version}.tar.gz
# Source0-md5:	77176f828ff333631c5293c387e72f82
URL:		http://harderware.bleedingmind.com/index.php?l=en&p=/mrplot
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mrplot is a general purpose plotting library written completely in
ruby. It has an interface to output plots using RMagick and can be
easily extended to support other output modules.

%description -l pl
mrplot to biblioteka ogólnego przeznaczenia do rysowania wykresów.
Dostarcza interfejs do tworzenia wykresów przy u¿yciu RMagick i jest
³atwo rozszerzalna na obs³ugê innych modu³ów.

%prep
%setup -q

%build
ruby install.rb config \
	--stdruby=%{ruby_rubylibdir} \
	--siteruby=%{ruby_rubylibdir} \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby install.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/%{name}
