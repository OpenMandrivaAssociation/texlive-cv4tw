Name:		texlive-cv4tw
Version:	34577
Release:	2
Summary:	LaTeX CV class, with extended details
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cv4tw
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv4tw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cv4tw.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/cv4tw
%doc %{_texmfdistdir}/doc/latex/cv4tw

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
