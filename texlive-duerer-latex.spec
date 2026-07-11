%global tl_name duerer-latex
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	LaTeX support for the Duerer fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/duerer-latex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX support for Hoenig's Computer Duerer fonts, using their standard
fontname names.

