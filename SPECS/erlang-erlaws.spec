%global realname erlaws
%global debug_package %{nil}


Name:		erlang-%{realname}
Version:	0.0.1
Release:	1%{?dist}
Summary:	Erlang Amazon WebServices
Group:		Development/Libraries
# Dual licensing (MPL or BSD) is explicitly stated at project's web-page
# log4erl_parser.erl is licensed under ERPL
License:	https://raw.github.com/x6j8x/erlaws/master/LICENSE
URL:		https://github.com/x6j8x/erlaws.git
Source0:	erlaws-0.0.1.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	erlang
Requires:	erlang


%description
Erlaws provides Erlang interfaces to various Amazon WebService offerings.


%prep
%setup -q -n %{realname}-%{version}
# in mochiweb

%build
mkdir ebin
erl -make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
mkdir -p $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/include
install -m 644 ebin/*.beam $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 include/*.hrl $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/include


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE
%dir %{_libdir}/erlang/lib/%{realname}-%{version}
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/include
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/*.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/include/*.hrl


%changelog
* Sun Jul 17 2011 Junichi Shinohara <tabe1hands@gmail.com> - 0.0.1-1
- Initial build

