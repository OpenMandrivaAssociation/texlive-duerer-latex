Name:		texlive-duerer-latex
Version:	15878
Release:	2
Summary:	LaTeX support for the Duerer fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/duerer-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX support for Hoenig's Computer Duerer fonts, using their
standard fontname names.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/duerer-latex/duerer.sty
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdin.fd
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdr.fd
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdss.fd
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdtt.fd
%doc %{_texmfdistdir}/doc/latex/duerer-latex/README
%doc %{_texmfdistdir}/doc/latex/duerer-latex/duerer.pdf
%doc %{_texmfdistdir}/doc/latex/duerer-latex/duerer.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
