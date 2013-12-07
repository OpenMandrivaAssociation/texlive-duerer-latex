# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/duerer-latex
# catalog-date 2008-08-18 13:49:16 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-duerer-latex
Version:	1.1
Release:	4
Summary:	LaTeX support for the Duerer fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/duerer-latex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer-latex.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751110
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718271
- texlive-duerer-latex
- texlive-duerer-latex
- texlive-duerer-latex
- texlive-duerer-latex

