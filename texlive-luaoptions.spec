Name:		texlive-luaoptions
Version:	64870
Release:	1
Summary:	Option handling for LuaLaTeX packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luaoptions
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaoptions.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaoptions.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LuaLaTeX package provides extensive support for handling
options, on package level and locally. It allows the
declaration of sets of options, along with defaults,
expected/allowed values and limited type checking. These
options can be enforced as package options, changed at any
point during a document, or overwritten locally by optional
macro arguments. It is also possible to instantiate an Options
object as an independent Lua object, without linking it to a
package. Luaoptions can be used to enforce and prepopulate
options, or it can be used to simply handle the parsing of
optional key=value arguments into proper Lua tables.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luaoptions
%doc %{_texmfdistdir}/doc/lualatex/luaoptions

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
