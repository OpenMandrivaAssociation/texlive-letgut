Name:		texlive-letgut
Version:	64618
Release:	2
Summary:	Class for the newsletter "La Lettre GUTenberg" of the French TeX User Group GUTenberg
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/letgut
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letgut.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letgut.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letgut.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The French TeX User Group GUTenberg has been publishing "The
GUTenberg Letter", its irregular newsletter, since February
1993. For this purpose, a dedicated, in-house (La)TeX class was
gradually created but, depending on new needs and on the people
who were publishing the Newsletter, its development was
somewhat erratic; in particular, it would not have been
possible to publish its code as it was. In addition, its
documentation was non-existent. The Board of Directors of the
association, elected in November 2020, wished to provide a
better structured, more perennial and documented class, able to
be published on the CTAN. This is now done with the present
'letgut' class. # French L'association GUTenberg publie "La
Lettre GUTenberg", son bulletin irregulomestriel, depuis
fevrier 1993. Pour ce faire, une classe (La)TeX dediee, maison,
a peu a peu vu le jour mais, au gre des nouveaux besoins et des
personnes qui ont assure la publication de la Lettre, son
developpement a ete quelque peu erratique ; il n'aurait
notamment pas ete possible de publier son code en l'etat. En
outre, sa documentation etait inexistante. Le Conseil
d'Administration de l'association, elu en novembre 2020, a
souhaite fournir une classe mieux structuree, davantage perenne
et documentee, a meme d'etre publiee sur le CTAN. C'est
desormais chose faite avec la presente classe letgut.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/letgut
%{_texmfdistdir}/tex/lualatex/letgut
%doc %{_texmfdistdir}/doc/lualatex/letgut

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
