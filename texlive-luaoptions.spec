%global tl_name luaoptions
%global tl_revision 79068

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	Option handling for LuaLaTeX packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luaoptions
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaoptions.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaoptions.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LuaLaTeX package provides extensive support for handling options,
on package level and locally. It allows the declaration of sets of
options, along with defaults, expected/allowed values and limited type
checking. These options can be enforced as package options, changed at
any point during a document, or overwritten locally by optional macro
arguments. It is also possible to instantiate an Options object as an
independent Lua object, without linking it to a package. Luaoptions can
be used to enforce and prepopulate options, or it can be used to simply
handle the parsing of optional key=value arguments into proper Lua
tables.

