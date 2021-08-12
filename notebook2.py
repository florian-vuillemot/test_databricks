# Databricks notebook source
r = dbutils.notebook.run("notebook1", 60)
dbutils.notebook.exit(int(r)*2)
