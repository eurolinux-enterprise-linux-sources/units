dnl        Copyright (C) 2006 Free Software Foundation, Inc
dnl Process this file with autoconf to produce a configure script.

AC_INIT(GNU units,2.01,adrianm@gnu.org)
AC_PREREQ(2.59)
AC_ARG_PROGRAM

AC_SUBST(DEFIS)
AC_SUBST(STRFUNC)
AC_SUBST(UDAT)

dnl Hack to set correct CFLAGS for cl compiler while still
dnl allowing user to override the CFLAGS setting

saveCFLAGS=$CFLAGS

AC_PROG_CC(gcc cc egcs cl.exe)
AC_PROG_CC_C99

if test "$CC" = cl.exe -a -z "$saveCFLAGS" ; then
    AC_MSG_NOTICE([setting special CFLAGS value for cl])
    CFLAGS="-G6 -O2 -Za -W3 -nologo"
fi

AC_C_CONST
AC_PROG_INSTALL

dnl Checks for libraries.

AC_SEARCH_LIBS(sin,m)

dnl Check for readline with various possible required support libs

AS_UNSET(ac_cv_lib_readline_readline)
for termlib in "" -ltermcap -lncurses -lcurses; do
  if test "$ac_cv_lib_readline_readline" != yes ; then
    AS_UNSET(ac_cv_lib_readline_readline)
    AC_CHECK_LIB(readline,readline,
                 [LIBS="-lreadline $termlib $LIBS";DEFIS="$DEFIS -DREADLINE"],
                 [],[$termlib])
  fi
done

dnl Checks for header files.
AC_CHECK_HEADER(string.h,[],[DEFIS="$DEFIS -DSTRINGS_H"])
AC_CHECK_HEADER(stdlib.h,[],[DEFIS="$DEFIS -DNO_STDLIB_H"])

dnl Checks for library functions.
AC_CHECK_FUNC(strchr,[],DEFIS="$DEFIS -DNO_STRCHR")
AC_CHECK_FUNC(strspn,[],DEFIS="$DEFIS -DNO_STRSPN";STRFUNC="strfunc.$OBJEXT")
AC_CHECK_FUNC(strtok,[],DEFIS="$DEFIS -DNO_STRTOK";STRFUNC="strfunc.$OBJEXT")

AC_CHECK_FUNC(setenv,[],DEFIS="$DEFIS -DNO_SETENV")
AC_CHECK_FUNC(setlocale,[],DEFIS="$DEFIS -DNO_SETLOCALE")

AC_CACHE_CHECK([for locale and UTF-8 support], am_cv_utf8,
  [AC_TRY_LINK([
#define _XOPEN_SOURCE 600
#include <wchar.h>
#include <locale.h>
#include <langinfo.h>
], [wchar_t *out;char *in;char *res;
     res=setlocale(LC_CTYPE,"");res=in; 
     mbsrtowcs(out, &res, 2, NULL);
     wcswidth(out,2);],
    am_cv_utf8=yes,
    am_cv_utf8=no)
])

if test $am_cv_utf8 = yes; then
    DEFIS="$DEFIS -DSUPPORT_UTF8"
fi

AC_CACHE_CHECK([for isfinite], am_cv_isfinite,
  [AC_TRY_LINK([
#define _XOPEN_SOURCE 600
#include <math.h>
], [float a;a=1;isfinite(a);],
    am_cv_isfinite=yes,
    am_cv_isfinite=no)
])

if test $am_cv_isfinite = no; then
    DEFIS="$DEFIS -DNO_ISFINITE"
fi


dnl Check for path search option
AC_ARG_ENABLE([path-search],
    AC_HELP_STRING([--enable-path-search],
       [search path for units database (default is NO)]),
    [UDAT=""],[UDAT="$datadir/units/"])

AC_CONFIG_FILES(Makefile)
AC_OUTPUT
