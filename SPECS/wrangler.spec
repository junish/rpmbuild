Name:		wrangler
Version:	0.9.3
Release:	1%{?dist}
Summary:	the Erlang Refactorer
Group:		Development/Libraries
License:	BSD
URL:		http://www.cs.kent.ac.uk/projects/wrangler/Home.html
Source0:	wrangler-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Wrangler is an interactive refactoring tool for Erlang, integrated into both emacs and Eclipse.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT/usr datadir=$RPM_BUILD_ROOT/usr/share
rm -rf $RPM_BUILD_ROOT/usr/share/wrangler/src/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/wrangler/bin/*
/usr/share/wrangler/ebin/*
/usr/share/wrangler/include/*
/usr/share/wrangler/elisp/*
/usr/share/wrangler/plt/*

%defattr(-,root,root,-)
%doc



%changelog
* Thu Jun 30 2011 Junichi Shinohara <tabe1hands@gmail.com> - 0.9.3-1
- Initial package
