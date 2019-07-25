#/usr/bin/Rscript

Sys.setenv(R_LIBS_USER = "/scratch/aksmiyazaki/Workdir/r_libs_user")
dir.create(path = Sys.getenv("R_LIBS_USER"), showWarnings = FALSE, recursive = TRUE)
.libPaths(c("/scratch/aksmiyazaki/Workdir/r_libs_user", .libPaths()))

install.packages("devtools", lib = Sys.getenv("R_LIBS_USER"))
library(devtools)
devtools::install_local(path="/scratch/aksmiyazaki/Workdir/starvz/R_package")
install.packages("sparklyr", lib = Sys.getenv("R_LIBS_USER"))
