%define   _base node

Name:	    %{_base}js
Version:	0.4.1
Release:	1%{?dist}
Summary:	Evented I/O for V8 Javascript.
Packager: Susan Potter <susan@managedopensource.com>
Vendor:   http://managedopensource.com

Group:		Development/Libraries
License:	MIT License
URL:		  http://nodejs.org/
Source0:	%{_base}-v%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  gcc	make

%description
Evented I/O for V8 Javascript.

%prep
%setup -q -n %{_base}-v%{version}


%build
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/node
/usr/bin/node-waf
/usr/include/node/config.h
/usr/include/node/eio.h
/usr/include/node/ev.h
/usr/include/node/node.h
/usr/include/node/node_buffer.h
/usr/include/node/node_config.h
/usr/include/node/node_events.h
/usr/include/node/node_object_wrap.h
/usr/include/node/node_version.h
/usr/include/node/v8-debug.h
/usr/include/node/v8-preparser.h
/usr/include/node/v8-profiler.h
/usr/include/node/v8-testing.h
/usr/include/node/v8.h
/usr/include/node/v8stdint.h
/usr/lib/node/wafadmin/Build.py
/usr/lib/node/wafadmin/Configure.py
/usr/lib/node/wafadmin/Constants.py
/usr/lib/node/wafadmin/Environment.py
/usr/lib/node/wafadmin/Logs.py
/usr/lib/node/wafadmin/Node.py
/usr/lib/node/wafadmin/Options.py
/usr/lib/node/wafadmin/Runner.py
/usr/lib/node/wafadmin/Scripting.py
/usr/lib/node/wafadmin/Task.py
/usr/lib/node/wafadmin/TaskGen.py
/usr/lib/node/wafadmin/Tools/__init__.py
/usr/lib/node/wafadmin/Tools/ar.py
/usr/lib/node/wafadmin/Tools/cc.py
/usr/lib/node/wafadmin/Tools/ccroot.py
/usr/lib/node/wafadmin/Tools/compiler_cc.py
/usr/lib/node/wafadmin/Tools/compiler_cxx.py
/usr/lib/node/wafadmin/Tools/compiler_d.py
/usr/lib/node/wafadmin/Tools/config_c.py
/usr/lib/node/wafadmin/Tools/cxx.py
/usr/lib/node/wafadmin/Tools/d.py
/usr/lib/node/wafadmin/Tools/dmd.py
/usr/lib/node/wafadmin/Tools/gas.py
/usr/lib/node/wafadmin/Tools/gcc.py
/usr/lib/node/wafadmin/Tools/gdc.py
/usr/lib/node/wafadmin/Tools/gnu_dirs.py
/usr/lib/node/wafadmin/Tools/gob2.py
/usr/lib/node/wafadmin/Tools/gxx.py
/usr/lib/node/wafadmin/Tools/icc.py
/usr/lib/node/wafadmin/Tools/icpc.py
/usr/lib/node/wafadmin/Tools/intltool.py
/usr/lib/node/wafadmin/Tools/libtool.py
/usr/lib/node/wafadmin/Tools/misc.py
/usr/lib/node/wafadmin/Tools/nasm.py
/usr/lib/node/wafadmin/Tools/node_addon.py
/usr/lib/node/wafadmin/Tools/osx.py
/usr/lib/node/wafadmin/Tools/preproc.py
/usr/lib/node/wafadmin/Tools/python.py
/usr/lib/node/wafadmin/Tools/suncc.py
/usr/lib/node/wafadmin/Tools/suncxx.py
/usr/lib/node/wafadmin/Tools/unittestw.py
/usr/lib/node/wafadmin/Tools/winres.py
/usr/lib/node/wafadmin/Tools/xlc.py
/usr/lib/node/wafadmin/Tools/xlcxx.py
/usr/lib/node/wafadmin/Utils.py
/usr/lib/node/wafadmin/__init__.py
/usr/lib/node/wafadmin/ansiterm.py
/usr/lib/node/wafadmin/pproc.py
/usr/lib/node/wafadmin/py3kfixes.py
/usr/lib/pkgconfig/nodejs.pc
%doc
/usr/share/man/man1/node.1.gz

%changelog
* Fri Feb 25 2011 - Junichi Shinohara <tabe1hadsn@gmail.com>
- node.js 0.4.1
* Tue Oct 19 2010 - susan@managedopensource.com
- Initial version of RPM specification file.
