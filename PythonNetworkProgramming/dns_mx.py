#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import dns.resolver

def resolve_hostname(hostname,indent=''):
	"Print an A and AAAA record for `hostname`;follow CNAMEs if necessary."
	indent =indent + '   '

	answer = dns.resolver.query(hostname,'A')
	if answer.rrset is not None:
		for record in answer:
			print(indent,hostname,'has A address1',record.address)
		return

	answer = dns.resolver.query(hostname,'AAAA')
	if answer.rrset is not None:
		for record in answer:
			print(indent,hostname,'has A address2',record.address)
		return

	answer = dns.resolver.query(hostname,'CNAME')
	if answer.rrset is not None:
		for record in answer:
			print(indent,hostname,'has A address3',record.address)
		return

def resolve_email_domain(domain):
	"For an email address `name@domain` find its mail server IP addresses."
	try:
		answer = dns.resolver.query(domain,'MX',raise_on_no_answer=False)
	except dns.resolver.NXDOMAIN:
		print('Error: No such domain',domain)
		return
	if answer.rrset is not None:
		records = sorted(answer,key=lambda record: record.preference)
		for record in records:
			name = record.exchange.to_text(omit_final_dot=True)
			print('Priority',record.preference)
			resolve_hostname(name)
	else:
		print('This domain has no explicit MX records')
		print('Attempting to resolve it as an A,AAAA,or CNAME')
		resolve_hostname(domain)

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Find mailserver IP address')
	parser.add_argument('domain',help='domain that you want to send mail to')
	resolve_email_domain(parser.parse_args().domain)
