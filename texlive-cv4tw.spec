# revision 32719
# category Package
# catalog-ctan /macros/latex/contrib/cv4tw
# catalog-date 2014-01-20 00:33:14 +0100
# catalog-license other-free
# catalog-version 0.1
Name:		texlive-cv4tw
Version:	0.1
Release:	5
Summary:	LaTeX CV class, with extended details
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cv4tw
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv4tw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv4tw.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class offers entries for assets and social networks;
customizable styles are provided. The class comes with no
documentation, but a worked example offers some guidance.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cv4tw/cv4tw-scheme.sty
%{_texmfdistdir}/tex/latex/cv4tw/cv4tw-theme-compact.sty
%{_texmfdistdir}/tex/latex/cv4tw/cv4tw-theme-core.sty
%{_texmfdistdir}/tex/latex/cv4tw/cv4tw-theme-sharp.sty
%{_texmfdistdir}/tex/latex/cv4tw/cv4tw-theme-simple.sty
%{_texmfdistdir}/tex/latex/cv4tw/cv4tw.cls
%doc %{_texmfdistdir}/doc/latex/cv4tw/sample-jules-verne.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
