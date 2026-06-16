import streamlit as st
from src.utils import load_css, get_image_path, log_streamlit_rerun
from src.prime_rsa import RsaEngine

# Terminal helper to know when streamlit restarts it's loop
log_streamlit_rerun()
load_css()

# Make RsaEngine available to Streamlit
rsa = RsaEngine()

st.header("Explore RSA Encryption")
st.image(get_image_path("thinking.gif"))
st.markdown(
    """
    RSA is a public-key encryption system. That means it uses:

    - a **public key** that can be shared openly
    - a **private key** that must be kept secret

    RSA helps solve a fundamental problem in secure communication: how can
    someone send you a secret message without first needing to share a secret
    password with you in person?

    This page walks through the building blocks of RSA one step at a time.
    You do not need any prior cryptography knowledge. We will start by choosing
    two prime numbers and use them to build the key pair.
    """
)
st.info(
    "Why primes? RSA takes advantage of the fact that it is easy to multiply two prime numbers together, "
    "but working backwards and factoring the result is much harder and computationally expensive."
)

st.subheader("Step 1: Choose Two Prime Numbers")
st.markdown(
    """
    Start by choosing two prime numbers, usually called **p** and **q**.
    A prime number can only be divided exactly by 1 and itself.

    In a real world implementation of RSA these primes are enormous. Here we use small values so you can
    see the mathematics clearly.
    """
)

prime_factor_one = st.select_slider(
    "Select a Prime (p)",
    options=rsa.prime_list,
    key="prime_one",
    value=rsa.prime_factor_p,
)
rsa.update_prime_p(prime_factor_one)

prime_factor_two = st.select_slider(
    "Select a Prime (q)",
    options=rsa.prime_list[1:],
    key="prime_two",
    value=rsa.prime_factor_q,
    help="Pick a second prime number to pair with p.",
)
rsa.update_prime_q(prime_factor_two)
modulus = prime_factor_one * prime_factor_two

st.subheader("Step 2: Build the Modulus")
st.markdown(
    """
    Next we multiply the two primes together to create **n**:

    - **n = p × q**

    This number, the modulus, becomes part of both the public key and the private key.
    """
)
st.latex(f'n = p * q = {prime_factor_one} * {prime_factor_two} = {modulus}')
st.markdown(
    f"""
    The modulus **n** helps set the size limit for messages in RSA.
    Before encryption, a message is converted into a number, and that number
    must be **smaller than n**.

    With your current values, the message number must be less than **{modulus}**.
    A larger modulus allows larger message blocks to be encrypted.
    """
)

st.subheader("Step 3: Calculate Euler's Totient")
st.markdown(
    """
    Now we calculate **Euler's totient**, written as **phi(n)**.

    When **p** and **q** are prime:

    - **phi(n) = (p - 1) × (q - 1)**

    This value is important because it helps us find two linked exponents:
    the public exponent **e** and the private exponent **d**.
    """
)
st.latex(f'\u03A6 (n)=(p-1) * (q-1)=({prime_factor_one}-1) * ({prime_factor_two}-1)= {prime_factor_one-1} * {prime_factor_two-1} = {rsa.totient}')
st.markdown(
    """
    Why does this work? **phi(n)** counts how many numbers below **n** are
    coprime to **n**, meaning they share no common factor with it.

    Because **n = p x q**, the only numbers that fail this test are the ones
    divisible by **p** or **q**. When **p** and **q** are prime, counting and
    removing those leaves exactly **(p - 1)(q - 1)** valid numbers.
    """
)

st.subheader("Step 4: Choose a Public Exponent")
st.markdown(
    f"""
    We now choose a public exponent **e**.

    Not every number will work. A valid **e** must be:

    - smaller than **phi(n)**
    - coprime with **phi(n)**, which means they share no common factors other than 1

    Based on your current choices of **p** and **q**, there are
    **{len(rsa.public_exponent_candidates)}** valid candidates.
    """
)
candidate_exponent = st.select_slider(
    "Select a public exponent (e)",
    options=rsa.public_exponent_candidates,
    key="candidate_exponent",
    value=rsa.public_exponent_candidates[0],
)
rsa.update_public_key(candidate_exponent)

st.subheader("Step 5: Calculate the Private Exponent")
st.markdown(
    """
    The private exponent is called **d**.

    d is chosen so that e × d leaves a remainder of 1 when divided by phi(n). 
    This makes d the modular inverse of e, and it is the mathematical relationship 
    that allows RSA decryption to reverse RSA encryption.

    Why this matters in RSA:

    The encryption and decryption exponents must be linked in exactly this way so that 
    raising a message to the power e and then to the power d brings you back to the original message.

    - the **public key** can be used to encrypt
    - the **private key** can be used to decrypt
    """
)

st.metric("Private exponent (d)", rsa.private_exponent)

st.subheader("RSA Values So Far")
col1, col2, col3, col4 = st.columns(4)
col1.metric("p", prime_factor_one)
col2.metric("q", prime_factor_two)
col3.metric("n", modulus)
col4.metric("phi(n)", rsa.totient)

st.markdown(
    f"""
    This values for the keys are:

    - Public key: **(n={modulus}, e={candidate_exponent})**
    - Private key: **(n={modulus}, d={rsa.private_exponent})**

    In a real RSA system, the public key can be shared with anyone, but the
    private key must stay secret.
    """
)

st.markdown("## Encrypting Messages")

st.image(get_image_path("rsa_encryption_keys.png"))
