#!/bash/env/python


class PII(object):
    def __init__(self, pattern, content):
        self.content = content
        self.pattern = pattern


class ArtifactsCollector(PII):
    # TODO: create
    def find_credit_card_numbers(self):
        """Find Credit Card Patterns"""
        pass

    # TODO: create
    def find_social_security_numbers(self):
        """Find Social Security Numbers"""
        pass

    # TODO: create
    def find_ipv4_adress(self):
        """Find IPv4 Addresses"""
        pass

    # TODO: create
    def find_ipv6_address(self):
        """find IPv6 Addresses"""
        pass

    # TODO: create
    def find_email_address(self):
        """Find Email Addresses"""
        pass

    # TODO: create
    def find_credientials(self):
        """Find Credentials"""
        pass

    # TODO: create
    def find_api_credentials(self):
        """Find API/Token/Secrets"""
        pass

    # TODO: create
    def find_rsa_artifacts(self):
        """Find key artifacts"""
        pass
