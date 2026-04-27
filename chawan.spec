Summary:	A text-mode web browser
Summary(pl.UTF-8):	Tekstowa przeglądarka www
Name:		chawan
Version:	0.3.3
Release:	1
License:	Public Domain
Group:		Applications/Networking
Source0:	https://git.sr.ht/~bptato/chawan/archive/v%{version}.tar.gz
# Source0-md5:	168a817cff5da13dc1cd03f53491d052
URL:		https://chawan.net/
BuildRequires:	nim >= 2.0.0
Requires:	/bin/sh
Requires:	brotli
Requires:	glibc
Requires:	libgcc
Requires:	libssh2
Requires:	openssl
Suggests:	mailcap
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A text-mode web browser and pager for Unix-like systems.

%description -l pl.UTF-8
Tekstowa przeglądarka www i pager dla systemów uniksowych.

%prep
%setup -q -n %{name}-v%{version}

%build
export CFLAGS="%{rpmcflags} -ffile-prefix-map=$(pwd)/="
%{__make} LIBEXECDIR=%{_prefix}/lib/chawan

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT" \
PREFIX='%{_prefix}' \
LIBEXECDIR="$RPM_BUILD_ROOT%{_prefix}/lib/chawan" \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cha
%attr(755,root,root) %{_bindir}/mancha
%dir %{_prefix}/lib/chawan
%dir %{_prefix}/lib/chawan/cgi-bin
%attr(755,root,root) %{_prefix}/lib/chawan/ansi2html
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/canvas
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/chabookmark
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/file
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/finger
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/ftp
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/gemini
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/gopher
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/http
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/jebp
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/man
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/nanosvg
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/resize
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/sftp
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/sixel
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/spartan
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/ssl
%attr(755,root,root) %{_prefix}/lib/chawan/cgi-bin/stbi
%attr(755,root,root) %{_prefix}/lib/chawan/dirlist2html
%attr(755,root,root) %{_prefix}/lib/chawan/gmi2html
%attr(755,root,root) %{_prefix}/lib/chawan/gopher2html
%attr(755,root,root) %{_prefix}/lib/chawan/img2html
%attr(755,root,root) %{_prefix}/lib/chawan/md2html
%attr(755,root,root) %{_prefix}/lib/chawan/nc
%attr(755,root,root) %{_prefix}/lib/chawan/tohtml
%attr(755,root,root) %{_prefix}/lib/chawan/uri2html
%attr(755,root,root) %{_prefix}/lib/chawan/urldec
%attr(755,root,root) %{_prefix}/lib/chawan/urlenc
%{_mandir}/man1/cha.1*
%{_mandir}/man1/mancha.1*
%{_mandir}/man5/cha-config.5*
%{_mandir}/man5/cha-localcgi.5*
%{_mandir}/man5/cha-mailcap.5*
%{_mandir}/man5/cha-mime.types.5*
%{_mandir}/man5/cha-urimethodmap.5*
%{_mandir}/man7/cha-api.7*
%{_mandir}/man7/cha-css.7*
%{_mandir}/man7/cha-image.7*
%{_mandir}/man7/cha-protocols.7*
%{_mandir}/man7/cha-terminal.7*
%{_mandir}/man7/cha-troubleshooting.7*
