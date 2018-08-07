setwd("path_to_my_directory")

genot <- read.table("genot.txt", sep = "\t", header = T)
genot_mat <- as.matrix(genot[, 2:ncol(genot)])
rownames(genot_mat) <- genot$Ind_id

phenot <- read.table("phenot.txt", sep = "\t", header = T)

map <- read.table("map.txt", sep = "\t", header = T)

PCs <- read.table("PCs.txt", sep = "\t", header = T)
PC_mat <- as.matrix(PCs[, 2:ncol(PCs)])
rownames(PC_mat) <- PCs$Ind_id

genot_imp <- genot_mat
average <- colMeans(genot_imp, na.rm = T)

for (i in 1:ncol(genot_imp)){
	genot_imp[is.na(genot_imp[,i]), i] <- average[i]
}

stdev <- apply(genot_imp, 2, sd)
genot_stand <- sweep(sweep(genot_imp, 2, average, "-"), 2, stdev, "/")
K_mat <- (genot_stand %*% t(genot_stand)) / ncol(genot_stand)

source("mlmm_cof.r")
source("emma.r")

mygwas <- mlmm_cof(Y = phenot$Phenot1, X = genot_imp, cofs = PC_mat, K = K_mat, nbchunks = 2, maxsteps = 10)
