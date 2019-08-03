#!/usr/bin/env Rscript

Sys.setenv(R_LIBS_USER = "/scratch/aksmiyazaki/Workdir/r_libs_user")
dir.create(path = Sys.getenv("R_LIBS_USER"), showWarnings = FALSE, recursive = TRUE)
.libPaths(c("/scratch/aksmiyazaki/Workdir/r_libs_user", .libPaths()))

#install.packages("Rcpp") # em caso de erro por essa biblioteca ser de outra versão
#install.package("rlang") # em caso de erro por essa biblioteca ser de outra versão
#install.package("glue") # em caso de erro por essa biblioteca ser de outra versão
#install.package("tidyselect") # em caso de erro por essa biblioteca ser de outra versão

install.packages("devtools", lib = Sys.getenv("R_LIBS_USER"))
library(devtools)
devtools::install_local(path="/scratch/aksmiyazaki/Workdir/starvz/R_package")
install.packages("sparklyr", lib = Sys.getenv("R_LIBS_USER"))
install.packages("remotes")
remotes::install_github("apache/arrow", subdir = "r", ref = "apache-arrow-0.14.0")

library(sparklyr)
spark_install("2.4.3")
