"""Check HIBP."""
import pypwned


def pwned_recon(email):
    """Check HIBP if email has been compromised."""
    results = pypwned.getAllBreachesForAccount(email=email)
    return results
