%define up_name  ocamlgsl

Name:           ocaml-%{up_name}
Version:        0.6.0
Release:        %mkrel 1
Summary:        GNU Scientific Library (GSL) for OCaml
License:        GPL
Group:          Development/Other
URL:            http://oandrieu.nerim.net/ocaml/gsl/
Source0:        http://oandrieu.nerim.net/ocaml/gsl/%{up_name}-%{version}.tar.gz
#Patch0:        cdf_handle_int_arguments.dpatch
Patch1:         match_gcc_4_2.dpatch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  libgsl-devel >= 1.9
BuildRequires:  ocaml-findlib
BuildRequires:  awk

%description
This is an interface to GSL (GNU scientific library), for the
Objective Caml language.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch1 -p1

%build
make all
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/gsl
make install-findlib

# mli files
install -m 0644 *.mli %{buildroot}%{_libdir}/ocaml/gsl/

# info files
mkdir -p %{buildroot}%{_infodir}
install -m 644 ocamlgsl.info* %{buildroot}%{_infodir}

%clean
rm -rf %{buildroot}


%post devel
/sbin/install-info %{_infodir}/ocamlgsl.info %{_infodir}/dir

%postun devel
/sbin/install-info --delete ocamlgsl %{_infodir}/dir


%files
%defattr(-,root,root)
%doc COPYING NEWS NOTES README
%dir %{_libdir}/ocaml/gsl
%{_libdir}/ocaml/gsl/META
%{_libdir}/ocaml/gsl/*.cma
%{_libdir}/ocaml/gsl/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc
%{_infodir}/*.info*
%{_libdir}/ocaml/gsl/*.a
%{_libdir}/ocaml/gsl/*.cmxa
%{_libdir}/ocaml/gsl/*.cmx
%{_libdir}/ocaml/gsl/*.mli

