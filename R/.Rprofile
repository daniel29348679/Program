# Set locale to utf8
is_uft8_support <- grepl(
    "UTF-8|utf8", Sys.getenv("LANG"),
    ignore.case = TRUE, perl = TRUE
) &&
    R.version$major >= 4L &&
    R.version$minor >= 2.0
if (is_uft8_support) {
    suppressWarnings(Sys.setlocale("LC_ALL", Sys.getenv("LANG")))
}
