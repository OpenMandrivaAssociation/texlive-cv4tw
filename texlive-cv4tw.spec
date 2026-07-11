%global tl_name cv4tw
%global tl_revision 34577

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	LaTeX CV class, with extended details
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cv4tw
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cv4tw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cv4tw.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class offers entries for assets and social networks; customizable
styles are provided. The class comes with no documentation, but a worked
example offers some guidance.

