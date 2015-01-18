#!/bin/bash


USERS=`aws iam list-users | grep -i username | cut -d: -f2 | awk -F'"' '{ print $2 }'`
account_id=`aws ec2 describe-security-groups | grep -i owner | head -1 | cut -d: -f2 | awk -F'"' '{ print $2 }'`

for user in $USERS;
do
		group=`aws iam list-groups-for-user --user-name $user | grep -i Name | cut -d: -f2 | awk -F'"' '{ print $2 }'`
		mfa_dev=`aws iam list-mfa-devices --user-name $user | grep -i serial | cut -d: -f2-9 | awk -F'"' '{ print $2 }'`
		has_pass=`aws iam get-login-profile --user-name $user > /dev/null 2>&1`

		if [[ $? -eq 0 ]]; then
			has_password="Password Enabled Account"
		else
			has_password="Password Disabled Account"
		fi

		if [[ "$mfa_dev" == "" ]]; then
			mfa_dev="No registered MFA device"
		else
			mfa_dev=`aws iam list-mfa-devices --user-name $user | grep -i serial | cut -d: -f2-9 | awk -F'"' '{ print $2 }'`
		fi

		if [[ "$group" == "" ]]; then
			echo $account_id " | " "no group" " | " $user " | " $has_password " | " $mfa_dev " | "
		else
			echo $account_id " | " $group " | " $user " | " $has_password " | " $mfa_dev " | "
		fi
done%
