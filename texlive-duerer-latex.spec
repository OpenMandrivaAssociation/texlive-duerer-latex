Name:		texlive-duerer-latex
Version:	1.1
Release:	1
Summary:	LaTeX support for the Duerer fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/duerer-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
LaTeX support for Hoenig's Computer Duerer fonts, using their
standard fontname names.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
