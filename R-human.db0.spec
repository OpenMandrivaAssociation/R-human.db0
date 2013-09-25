%global packname  human.db0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.9.0
Release:          1
Summary:          Base Level Annotation databases for human
Group:            Sciences/Mathematics
License:          The Artistic License, Version 2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/human.db0_2.9.0.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods R-AnnotationDbi 
Requires:         R-methods R-AnnotationDbi 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-AnnotationDbi
BuildRequires:    R-methods R-AnnotationDbi 

%description
Base annotation databases for human, intended ONLY to be used by
AnnotationDbi to produce regular annotation packages.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
