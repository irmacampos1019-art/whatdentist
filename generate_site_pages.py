import os

def create_directories():
    os.makedirs('/app/sites/whatdentist/dentist', exist_ok=True)

def generate_pages():
    create_directories()

    # Shared parts
    header_html = """<header><div class="header-inner"><a href="/" class="logo">what<span>dentist</span></a><nav><ul><li><a href="/los-algodones">Los Algodones</a></li><li><a href="/tijuana">Tijuana</a></li><li><a href="/cancun">Cancun</a></li><li><a href="/pricing">Pricing</a></li><li><a href="/get-listed">Get Listed</a></li><li><a href="/contact">Contact</a></li></ul></nav><a href="https://wa.me/19283744575" class="btn btn-green">💬 WhatsApp</a><button class="mobile-menu-btn">☰</button></div></header>"""

    footer_html = """<footer>
  <div class="footer-grid">
    <div>
      <h4>whatdentist</h4>
      <p>The trusted dental directory for Mexico dental tourism. Find verified, board-certified dentists.</p>
      <p style="margin-top: 12px;">📞 <a href="tel:+19283744575">928-374-4575</a></p>
      <p>💬 <a href="https://wa.me/19283744575">WhatsApp Us</a></p>
    </div>
    <div>
      <h4>Cities</h4>
      <ul>
        <li><a href="/los-algodones">Los Algodones</a></li>
        <li><a href="/tijuana">Tijuana</a></li>
        <li><a href="/cancun">Cancun</a></li>
      </ul>
    </div>
    <div>
      <h4>For Dentists</h4>
      <ul>
        <li><a href="/get-listed">Get Listed</a></li>
        <li><a href="/pricing">Pricing Plans</a></li>
        <li><a href="/claim-profile">Claim Your Profile</a></li>
      </ul>
    </div>
    <div>
      <h4>Resources</h4>
      <ul>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/about">About Us</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 whatdentist.com.mx — Verified Dental Directory for Mexico</p>
  </div>
</footer>

<a href="https://wa.me/19283744575" class="whatsapp-float" title="Chat on WhatsApp">💬</a>

<script>
  // Mobile menu toggle script for responsiveness
  document.querySelector('.mobile-menu-btn').addEventListener('click', function() {
    const navUl = document.querySelector('nav ul');
    if (navUl.style.display === 'flex') {
      navUl.style.display = 'none';
    } else {
      navUl.style.display = 'flex';
      navUl.style.flexDirection = 'column';
      navUl.style.position = 'absolute';
      navUl.style.top = '70px';
      navUl.style.left = '0';
      navUl.style.width = '100%';
      navUl.style.background = '#ffffff';
      navUl.style.padding = '20px';
      navUl.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
      navUl.style.borderBottom = '2px solid var(--primary)';
      navUl.style.zIndex = '999';
    }
  });
</script>
"""

    head_meta_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="{robots}">
  
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  
  <link rel="stylesheet" href="/css/styles.css">
  {schema_tag}
</head>
<body>
"""

    # 1. los-algodones.html
    los_algodones_schema = """<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://whatdentist.com.mx/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Los Algodones",
        "item": "https://whatdentist.com.mx/los-algodones"
      }
    ]
  }
  </script>"""

    los_algodones_content = """
<section class="hero" style="background: linear-gradient(135deg, #1e40af 0%, #06b6d4 100%);">
  <div class="container">
    <h1>Top Dentists in Los Algodones, Mexico</h1>
    <p>Compare verified credentials, actual prices, and patient reviews for the best dentists in Molar City.</p>
  </div>
</section>

<section>
  <div class="container">
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start;">
      <div>
        <h2>Why Los Algodones is the Dental Tourism Capital</h2>
        <div style="font-size: 1.05rem; color: #334155; line-height: 1.7; display: flex; flex-direction: column; gap: 16px;">
          <p>
            <strong>Los Algodones, Mexico</strong>, is widely known as <strong>"Molar City"</strong> and is the undisputed capital of dental tourism in the world. Located just next to the US border, directly across from Andrade, California, and a few miles from Yuma, Arizona, this tiny town of about 6,000 residents boasts over 350 dental clinics and more than 1,000 highly trained dentists. Every day, thousands of Americans and Canadians walk or drive across the border to access world-class dental care at a fraction of the cost they would pay at home.
          </p>
          <p>
            Why is Los Algodones so popular? The primary reason is cost. Dental procedures in Los Algodones are between <strong>50% and 70% cheaper</strong> than in the United States and Canada. For instance, a single dental implant that would easily cost $4,000 in Phoenix or San Diego costs around $800 to $1,000 in Los Algodones. A high-quality porcelain or zirconia crown is available for $350 to $450, compared to $1,200 or more in the US.
          </p>
          <p>
            Safety and quality are also significant factors. Many dentists in Los Algodones have received their training or advanced certifications at prestigious universities in the United States and Europe, such as Loma Linda University, Harvard, and the International Congress of Oral Implantologists (ICOI). These clinics use state-of-the-art dental technology, including 3D CT scans, CAD/CAM digital imaging, and dental lasers, which are often newer than what many local family dentists in the US use.
          </p>
          <p>
            In addition to world-class care, Los Algodones offers unparalleled convenience. The border crossing at Andrade is extremely easy to navigate, with secure parking lots available on the US side for a nominal daily fee. Most dental clinics are located within walking distance of the border crossing, making it easy to walk over for an appointment and walk back to your car or hotel in Yuma. The local economy is entirely centered around dental tourism, pharmacies, and optical services, meaning that English is spoken fluently by virtually every professional, receptionist, and store clerk.
          </p>
          <p>
            Patients can also enjoy a vibrant, friendly atmosphere. There are excellent local cafes, restaurants serving authentic Mexican cuisine, and shops offering handmade crafts. For those receiving extensive work like dental implants or All-on-4 full-mouth reconstructions, the process is streamlined to minimize travel. Most clinics have their own in-house dental laboratories, which means crowns, veneers, and dentures can be manufactured and fitted in days rather than weeks.
          </p>
          <p>
            Choosing the right dentist is essential, and directories like <strong>whatdentist.com.mx</strong> make it easy by providing transparent pricing, verifying credentials against official Mexican registries (such as the Cédula Profesional system), and offering honest, verified patient reviews. Whether you need a simple cleaning, root canal, cosmetic veneers, or a complete implant-supported smile makeover, Los Algodones is a safe, highly affordable, and world-renowned destination that can save you thousands of dollars while giving you a healthy, beautiful smile.
          </p>
        </div>

        <h2 style="margin-top: 40px;">Dentist Listings in Los Algodones</h2>
        <div class="dentist-grid" style="grid-template-columns: 1fr; gap: 32px;">
          <!-- Dr. Moguel Card -->
          <div class="dentist-card" style="display: grid; grid-template-columns: 300px 1fr; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; background: #fff;">
            <img src="https://media.base44.com/images/public/6a5301f7d191f37052971c5e/7483864c6_Dr-Jose-Moguel-Dental-Implant-Expertise-in-Mexico-los-algodones.webp" alt="Dr. José Moguel" style="width: 100%; height: 100%; object-fit: cover;">
            <div style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; gap: 8px; margin-bottom: 12px;">
                  <span class="badge badge-featured" style="margin:0;">⭐ Featured</span>
                  <span class="badge badge-verified" style="margin:0;">✓ Verified</span>
                </div>
                <h3 style="margin: 0 0 8px 0; font-size: 1.5rem; color: var(--dark);">Dr. José Moguel</h3>
                <p class="specialty" style="margin: 0 0 12px 0; font-size: 1rem;">Dental Implants • All-on-4 • 3-ON-8™ • Periodontics</p>
                <p class="rating" style="margin: 0 0 12px 0;">⭐ 5.0 (847 reviews)</p>
                <p class="city" style="margin: 0 0 12px 0;">📍 Los Algodones, Baja California</p>
                <p style="color: var(--gray); font-size: 0.95rem; margin-bottom: 20px;">Over 15 years of expert clinical experience specializing in high-quality dental implants and complex full-mouth reconstructions.</p>
              </div>
              <div class="actions" style="padding: 0; border: none; margin-top: auto; display: flex; gap: 12px;">
                <a href="/dentist/dr-jose-moguel" class="btn btn-primary" style="flex: 1;">View Profile</a>
                <a href="https://wa.me/19283744575" class="btn btn-green" style="flex: 1;">💬 Contact</a>
              </div>
            </div>
          </div>

          <!-- Dr. Sevilla Card -->
          <div class="dentist-card" style="display: grid; grid-template-columns: 300px 1fr; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; background: #fff;">
            <div style="height: 100%; background: linear-gradient(135deg, #2563eb, #06b6d4); display: flex; align-items: center; justify-content: center; color: white; font-size: 4rem; font-weight: 800; min-height: 250px;">DS</div>
            <div style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="display: flex; gap: 8px; margin-bottom: 12px;">
                  <span class="badge badge-featured" style="margin:0;">⭐ Featured</span>
                  <span class="badge badge-pending" style="margin:0;">⏳ Pending Verification</span>
                </div>
                <h3 style="margin: 0 0 8px 0; font-size: 1.5rem; color: var(--dark);">Dr. Jonatan Sevilla</h3>
                <p class="specialty" style="margin: 0 0 12px 0; font-size: 1rem;">Veneers • Crowns • Smile Makeovers • Cosmetic Dentistry</p>
                <p class="rating" style="margin: 0 0 12px 0;">⭐ 4.9 (312 reviews)</p>
                <p class="city" style="margin: 0 0 12px 0;">📍 Los Algodones, Baja California</p>
                <p style="color: var(--gray); font-size: 0.95rem; margin-bottom: 20px;">Dedicated cosmetic dental specialist focused on veneers, custom porcelain crowns, and dazzling smile makeovers.</p>
              </div>
              <div class="actions" style="padding: 0; border: none; margin-top: auto; display: flex; gap: 12px;">
                <a href="/dentist/dr-jonatan-sevilla" class="btn btn-primary" style="flex: 1;">View Profile</a>
                <a href="https://wa.me/19283744575" class="btn btn-green" style="flex: 1;">💬 Contact</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Cost Table Sidebar -->
      <div style="background: var(--white); padding: 24px; border-radius: 12px; border: 1px solid #e2e8f0; position: sticky; top: 100px;">
        <h3 style="margin-bottom: 16px; color: var(--primary);">Cost Comparison Table</h3>
        <p style="color: var(--gray); font-size: 0.9rem; margin-bottom: 16px;">See how much you can save on high-quality dental care in Los Algodones compared to the United States and Canada.</p>
        <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
          <thead>
            <tr style="border-bottom: 2px solid #e2e8f0;">
              <th style="padding: 8px 0;">Procedure</th>
              <th style="padding: 8px; text-align: right; color: var(--gray);">US / CA</th>
              <th style="padding: 8px; text-align: right; color: var(--green); font-weight: 700;">Algodones</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid #f1f5f9;">
              <td style="padding: 8px 0; font-weight: 500;">Dental Implant</td>
              <td style="padding: 8px; text-align: right; text-decoration: line-through; color: var(--gray);">$4,000</td>
              <td style="padding: 8px; text-align: right; color: var(--green); font-weight: 700;">$800</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9;">
              <td style="padding: 8px 0; font-weight: 500;">Porcelain Crown</td>
              <td style="padding: 8px; text-align: right; text-decoration: line-through; color: var(--gray);">$1,200</td>
              <td style="padding: 8px; text-align: right; color: var(--green); font-weight: 700;">$350</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9;">
              <td style="padding: 8px 0; font-weight: 500;">All-on-4 System</td>
              <td style="padding: 8px; text-align: right; text-decoration: line-through; color: var(--gray);">$24,000</td>
              <td style="padding: 8px; text-align: right; color: var(--green); font-weight: 700;">$8,000</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9;">
              <td style="padding: 8px 0; font-weight: 500;">Root Canal + Post</td>
              <td style="padding: 8px; text-align: right; text-decoration: line-through; color: var(--gray);">$1,100</td>
              <td style="padding: 8px; text-align: right; color: var(--green); font-weight: 700;">$250</td>
            </tr>
            <tr style="border-bottom: 1px solid #f1f5f9;">
              <td style="padding: 8px 0; font-weight: 500;">Teeth Whitening</td>
              <td style="padding: 8px; text-align: right; text-decoration: line-through; color: var(--gray);">$500</td>
              <td style="padding: 8px; text-align: right; color: var(--green); font-weight: 700;">$150</td>
            </tr>
            <tr>
              <td style="padding: 8px 0; font-weight: 500;">Bone Graft</td>
              <td style="padding: 8px; text-align: right; text-decoration: line-through; color: var(--gray);">$800</td>
              <td style="padding: 8px; text-align: right; color: var(--green); font-weight: 700;">$300</td>
            </tr>
          </tbody>
        </table>
        <div style="background: var(--light-gray); padding: 12px; border-radius: 8px; margin-top: 16px; text-align: center;">
          <p style="font-weight: 700; color: var(--dark); margin-bottom: 8px; font-size: 0.9rem;">Need to speak with a dentist?</p>
          <a href="https://wa.me/19283744575" class="btn btn-green" style="display: block; font-size: 0.85rem; padding: 8px 16px;">💬 WhatsApp 928-374-4575</a>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="cta-bar">
  <div class="container">
    <h2>Are You a Dentist in Los Algodones?</h2>
    <p style="margin-top: 12px; font-size: 1.1rem;">Connect with US and Canadian patients searching for high-quality care. Get listed today.</p>
    <a href="/get-listed">Get Listed — It's Free →</a>
  </div>
</div>
"""

    # Write Page 1
    with open('/app/sites/whatdentist/los-algodones.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Top Dentists in Los Algodones, Mexico | Verified Reviews & Prices",
            description="Find verified, top-rated dentists in Los Algodones (Molar City), Mexico. Compare dental procedures, see actual prices, and read trusted reviews.",
            canonical="https://whatdentist.com.mx/los-algodones",
            robots="index, follow",
            schema_tag=los_algodones_schema
        ))
        f.write(header_html)
        f.write(los_algodones_content)
        f.write(footer_html)

    # 2. tijuana.html
    tijuana_content = """
<section class="hero" style="background: linear-gradient(135deg, #1e40af 0%, #06b6d4 100%);">
  <div class="container">
    <h1>Top Dentists in Tijuana, Mexico</h1>
    <p>Find trusted, board-certified dental clinics and save up to 75% just minutes across the San Diego border.</p>
  </div>
</section>

<section>
  <div class="container">
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start;">
      <div>
        <h2>Tijuana: World-Class Dental Care Minutes from San Diego</h2>
        <div style="font-size: 1.05rem; color: #334155; line-height: 1.7; display: flex; flex-direction: column; gap: 16px;">
          <p>
            <strong>Tijuana, Mexico</strong>, has grown to become one of the premier hubs for medical and dental tourism in North America. Situated directly on the border with California, just a short 15-minute drive from downtown San Diego, Tijuana is an incredibly convenient destination for patients seeking high-quality, affordable dental care. For decades, patients from California, Arizona, Oregon, and beyond have chosen Tijuana for everything from routine cleanings to advanced dental implant surgeries and cosmetic smile makeovers.
          </p>
          <p>
            One of Tijuana's primary appeals is its proximity and ease of access. The San Ysidro border crossing is the busiest land border in the world, and many modern dental clinics in Tijuana offer complimentary shuttle services directly from the border or from San Diego International Airport to make the transit seamless. For those who prefer to drive, secure parking and FastPass lane access (which significantly cuts down border wait times when returning to the US) are frequently provided by top dental offices.
          </p>
          <p>
            The cost savings in Tijuana are extraordinary. On average, patients save between <strong>60% and 75% on major dental procedures</strong>. Full-mouth restorations like All-on-4 or All-on-6 implant systems, which can exceed $25,000 per arch in the United States, are regularly performed in Tijuana's top-tier clinics for around $8,000 to $10,000 using the exact same FDA-approved materials and implants (such as Nobel Biocare or Straumann). Root canals, crowns, and orthodontic treatments like Invisalign are also available at highly competitive rates, making excellent oral health accessible to everyone.
          </p>
          <p>
            Beyond the financial savings, Tijuana features some of the most technologically advanced dental clinics in the world. Many practices are housed in state-of-the-art medical towers, such as the NewCity Medical Plaza, which offer luxury amenities, bilingual staff, and strict international sterilization protocols. Tijuana's dentists are highly educated, with many holding degrees and active memberships in international organizations like the American Dental Association (ADA) and the American Academy of Cosmetic Dentistry (AACD).
          </p>
          <p>
            While visiting Tijuana for dental work, patients can also experience the city's remarkable cultural and culinary renaissance. Known for its world-renowned "Baja Med" cuisine, craft breweries, art galleries, and vibrant neighborhoods, Tijuana offers a rich and exciting travel experience. Patients receiving multi-day treatments can stay in high-end, comfortable hotels close to their clinics, enjoying premium service and hospitality.
          </p>
          <p>
            At <strong>whatdentist.com.mx</strong>, our mission is to simplify your search for the best dental care in Tijuana. We are currently building and verifying our list of Tijuana dentists to ensure that every provider listed meets our rigorous criteria for licensing, education, safety, and transparent pricing. Tijuana continues to set the standard for border dental tourism, combining convenience, outstanding quality, and unmatched value for patients from all walks of life.
          </p>
        </div>

        <h2 style="margin-top: 40px;">Dentist Listings</h2>
        
        <!-- Coming Soon Block -->
        <div style="background: var(--white); border: 2px dashed var(--primary); padding: 40px; border-radius: 12px; text-align: center; margin-top: 20px;">
          <span style="font-size: 3rem;">⏳</span>
          <h3 style="margin-top: 16px; color: var(--primary); font-size: 1.5rem;">Tijuana Directory Coming Soon</h3>
          <p style="color: var(--gray); max-width: 500px; margin: 12px auto 24px;">Our clinical team is currently auditing and verifying Tijuana-based dental clinics to guarantee they meet our high standard of credentialing and transparency.</p>
          <div style="display: flex; justify-content: center; gap: 16px;">
            <a href="/get-listed" class="btn btn-primary">Are You a Tijuana Dentist? Get Listed</a>
            <a href="/contact" class="btn btn-green">Request a Tijuana Recommendation</a>
          </div>
        </div>
      </div>

      <!-- Cost comparison short sidebar -->
      <div style="background: var(--white); padding: 24px; border-radius: 12px; border: 1px solid #e2e8f0; position: sticky; top: 100px;">
        <h3 style="margin-bottom: 12px; color: var(--primary);">Quick Savings Guide</h3>
        <p style="color: var(--gray); font-size: 0.95rem; margin-bottom: 16px;">Average savings on standard treatments in Tijuana:</p>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 12px;">
          <li style="display: flex; justify-content: space-between; border-bottom: 1px solid #f1f5f9; padding-bottom: 8px;">
            <span>Single Implant</span>
            <span style="color: var(--green); font-weight: 700;">Save ~70%</span>
          </li>
          <li style="display: flex; justify-content: space-between; border-bottom: 1px solid #f1f5f9; padding-bottom: 8px;">
            <span>Zirconia Crown</span>
            <span style="color: var(--green); font-weight: 700;">Save ~65%</span>
          </li>
          <li style="display: flex; justify-content: space-between; border-bottom: 1px solid #f1f5f9; padding-bottom: 8px;">
            <span>All-on-4 System</span>
            <span style="color: var(--green); font-weight: 700;">Save ~68%</span>
          </li>
          <li style="display: flex; justify-content: space-between; border-bottom: 1px solid #f1f5f9; padding-bottom: 8px;">
            <span>Veneers (Set of 6)</span>
            <span style="color: var(--green); font-weight: 700;">Save ~60%</span>
          </li>
        </ul>
        <div style="background: var(--light-gray); padding: 16px; border-radius: 8px; margin-top: 20px; text-align: center;">
          <p style="font-size: 0.9rem; font-weight: 600; color: var(--dark);">Have questions? Talk to us.</p>
          <p style="font-size: 0.85rem; color: var(--gray); margin-bottom: 12px;">We help connect you with vetted dental professionals.</p>
          <a href="tel:+19283744575" style="font-weight: 700; color: var(--primary);">📞 928-374-4575</a>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="cta-bar">
  <div class="container">
    <h2>Connect with Verified Mexican Dentists</h2>
    <p style="margin-top: 12px; font-size: 1.1rem;">Search across top dental destinations. Direct patient-dentist interaction, no hidden commissions.</p>
    <a href="/get-listed">List Your Clinic for Free →</a>
  </div>
</div>
"""

    # Write Page 2
    with open('/app/sites/whatdentist/tijuana.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Top Dentists in Tijuana, Mexico | Verified Dental Directory",
            description="Looking for the best dentist in Tijuana, Mexico? Read verified reviews, compare dental treatment costs, and check board certifications. Listings coming soon.",
            canonical="https://whatdentist.com.mx/tijuana",
            robots="index, follow",
            schema_tag=""
        ))
        f.write(header_html)
        f.write(tijuana_content)
        f.write(footer_html)

    # 3. cancun.html
    cancun_content = """
<section class="hero" style="background: linear-gradient(135deg, #1e40af 0%, #06b6d4 100%);">
  <div class="container">
    <h1>Top Dentists in Cancun, Mexico</h1>
    <p>Combine high-quality dental care with an unforgettable Caribbean vacation and save up to 75%.</p>
  </div>
</section>

<section>
  <div class="container">
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start;">
      <div>
        <h2>Cancun: The Ultimate Destination for a "Dental Vacation"</h2>
        <div style="font-size: 1.05rem; color: #334155; line-height: 1.7; display: flex; flex-direction: column; gap: 16px;">
          <p>
            <strong>Cancun, Mexico</strong>, is famous worldwide for its turquoise waters, white sandy beaches, and luxurious all-inclusive resorts. However, in recent years, it has also emerged as one of the fastest-growing destinations for dental tourism. The concept of "dental vacation" is perfectly realized here, allowing patients from the United States, Canada, and the United Kingdom to combine essential dental treatments with a relaxing, tropical holiday—all while saving thousands of dollars.
          </p>
          <p>
            The financial incentive for traveling to Cancun for dental care is immense. Savings typically range from <strong>50% to 70% compared to North American and European prices</strong>. For instance, a complete smile makeover with custom porcelain veneers that would cost upwards of $15,000 in Canada or the US is available in Cancun for $5,000 to $6,000. These substantial savings easily cover the cost of flights, hotel stays, and dining, with plenty of money left over.
          </p>
          <p>
            Accreditation and expertise are cornerstone features of Cancun's top dental clinics. The city's leading dental professionals are board-certified, and many have undergone extensive postgraduate training in the United States and Europe. Because they cater to a high volume of international patients, Cancun clinics adhere strictly to international sanitation and safety standards, including those set by the American Dental Association (ADA) and OSHA. They utilize advanced dental technologies such as digital intraoral scanners, 3D cone-beam computed tomography (CBCT), and on-site dental labs to deliver precise, fast results.
          </p>
          <p>
            The logistics of a dental trip to Cancun are incredibly straightforward. Cancun International Airport is a major global hub, offering direct, low-cost flights from dozens of cities across the US, Canada, and Europe daily. Most dental clinics are located in the safe, modern Downtown area or right in the Hotel Zone, and many provide complimentary airport transfers and clinic shuttle services.
          </p>
          <p>
            For patients undergoing complex dental procedures, such as implants, bone grafts, or full-mouth reconstruction, Cancun offers a serene environment to recover. Spending your post-treatment days lounging by a resort pool or listening to the ocean waves is a far more pleasant healing experience than returning immediately to a busy work routine at home.
          </p>
          <p>
            At <strong>whatdentist.com.mx</strong>, we understand that traveling abroad for dental care requires trust. That is why we are currently in the process of auditing and verifying Cancun’s premier dental practices. Our upcoming directory for Cancun will feature only pre-vetted dentists who offer certified credentials, transparent pricing structures, and exceptional customer service. By combining world-class clinical expertise with the world's favorite beach destination, Cancun offers an unbeatable value proposition for anyone looking to restore their smile and their confidence.
          </p>
        </div>

        <h2 style="margin-top: 40px;">Dentist Listings</h2>
        
        <!-- Coming Soon Block -->
        <div style="background: var(--white); border: 2px dashed var(--primary); padding: 40px; border-radius: 12px; text-align: center; margin-top: 20px;">
          <span style="font-size: 3rem;">🏖️</span>
          <h3 style="margin-top: 16px; color: var(--primary); font-size: 1.5rem;">Cancun Directory Coming Soon</h3>
          <p style="color: var(--gray); max-width: 500px; margin: 12px auto 24px;">We are currently auditing state-of-the-art clinics in Cancun to guarantee they match our rigorous standards of transparency, safety, and certification.</p>
          <div style="display: flex; justify-content: center; gap: 16px;">
            <a href="/get-listed" class="btn btn-primary">Are You a Cancun Dentist? Get Listed</a>
            <a href="/contact" class="btn btn-green">Request a Cancun Recommendation</a>
          </div>
        </div>
      </div>

      <!-- Cancun short sidebar -->
      <div style="background: var(--white); padding: 24px; border-radius: 12px; border: 1px solid #e2e8f0; position: sticky; top: 100px;">
        <h3 style="margin-bottom: 12px; color: var(--primary);">The Dental Vacation</h3>
        <p style="color: var(--gray); font-size: 0.95rem; margin-bottom: 16px;">How to plan your dental trip to Cancun:</p>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 12px; font-size: 0.9rem;">
          <li style="display: flex; gap: 10px;">
            <span>1️⃣</span>
            <span><strong>Send X-Rays:</strong> Share your local treatment plan & X-rays with Cancun clinics for a virtual quote.</span>
          </li>
          <li style="display: flex; gap: 10px;">
            <span>2️⃣</span>
            <span><strong>Book Flights:</strong> Cancun has direct flights from all major US and Canadian cities.</span>
          </li>
          <li style="display: flex; gap: 10px;">
            <span>3️⃣</span>
            <span><strong>Enjoy & Heal:</strong> Get treated in modern clinics, and recover comfortably by the beach.</span>
          </li>
        </ul>
        <div style="background: var(--light-gray); padding: 16px; border-radius: 8px; margin-top: 20px; text-align: center;">
          <p style="font-size: 0.9rem; font-weight: 600; color: var(--dark); margin-bottom: 8px;">Need assistance?</p>
          <p style="font-size: 0.8rem; color: var(--gray); margin-bottom: 12px;">Speak directly with our team to find vetted options.</p>
          <a href="tel:+19283744575" style="font-weight: 700; color: var(--primary);">📞 928-374-4575</a>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="cta-bar">
  <div class="container">
    <h2>Restore Your Smile in Mexico</h2>
    <p style="margin-top: 12px; font-size: 1.1rem;">Verified directories make dental tourism safe and worry-free. Start your journey today.</p>
    <a href="/get-listed">List Your Clinic for Free →</a>
  </div>
</div>
"""

    # Write Page 3
    with open('/app/sites/whatdentist/cancun.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Top Dentists in Cancun, Mexico | Verified Dental Directory",
            description="Plan a dental vacation to Cancun, Mexico! Find verified dental specialists, save up to 70% on implants, crowns, and veneers, and recover on beautiful beaches.",
            canonical="https://whatdentist.com.mx/cancun",
            robots="index, follow",
            schema_tag=""
        ))
        f.write(header_html)
        f.write(cancun_content)
        f.write(footer_html)

    # 4. pricing.html
    pricing_content = """
<section class="hero" style="background: linear-gradient(135deg, #1e40af 0%, #06b6d4 100%);">
  <div class="container">
    <h1>Listing Plans for Dentists</h1>
    <p>Grow your clinic's patient roster by listing your practice on Mexico's most trusted independent dental tourism directory.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2 style="text-align: center; margin-bottom: 40px;">Choose a Plan to Grow Your Practice</h2>
    
    <div class="pricing-grid">
      <div class="pricing-card">
        <div class="plan-name" style="font-size: 1.4rem; color: var(--gray);">Free</div>
        <div class="price" style="color: var(--dark);">$0<span style="font-size:1rem; font-weight:400;">/mo</span></div>
        <p style="color: var(--gray); font-size: 0.9rem; margin-bottom: 16px;">Standard entry-level profile for dental clinics in Mexico.</p>
        <ul style="border-top: 1px solid #f1f5f9; padding-top: 16px;">
          <li>Basic profile listing</li>
          <li>1 city selection</li>
          <li>Basic Contact Form</li>
          <li>Unverified profile status</li>
        </ul>
        <a href="/get-listed?plan=free" class="btn btn-primary" style="display: block; margin-top: 24px; text-decoration: none;">Get Listed</a>
      </div>

      <div class="pricing-card" style="border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <div class="plan-name" style="font-size: 1.4rem; color: var(--primary);">Verified</div>
        <div class="price" style="color: var(--primary);">$29<span style="font-size:1rem; font-weight:400; color: var(--gray);">/mo</span></div>
        <p style="color: var(--gray); font-size: 0.9rem; margin-bottom: 16px;">Build trust with the highly sought-after Verified badge.</p>
        <ul style="border-top: 1px solid #f1f5f9; padding-top: 16px;">
          <li><strong>Verified Seal Badge</strong></li>
          <li>2 cities listed</li>
          <li>Photo gallery (up to 10 images)</li>
          <li>Detailed Procedure Price List</li>
          <li>Real Patient Reviews enabled</li>
        </ul>
        <a href="/get-listed?plan=verified" class="btn btn-primary" style="display: block; margin-top: 24px; text-decoration: none;">Get Verified</a>
      </div>

      <div class="pricing-card featured" style="border: 3px solid var(--primary); box-shadow: 0 10px 25px rgba(37,99,235,0.15);">
        <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: var(--primary); color: white; padding: 4px 16px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">Most Popular</div>
        <div class="plan-name" style="font-size: 1.4rem; color: var(--primary-dark);">Premium</div>
        <div class="price" style="color: var(--primary-dark);">$49<span style="font-size:1rem; font-weight:400; color: var(--gray);">/mo</span></div>
        <p style="color: var(--gray); font-size: 0.9rem; margin-bottom: 16px;">Stand out with priority ranking and rich visual galleries.</p>
        <ul style="border-top: 1px solid #f1f5f9; padding-top: 16px;">
          <li>Everything in Verified</li>
          <li>5 cities listed</li>
          <li>Before/after photos upload</li>
          <li><strong>Featured placement on pages</strong></li>
          <li>Priority placement in searches</li>
        </ul>
        <a href="/get-listed?plan=premium" class="btn btn-primary" style="display: block; margin-top: 24px; text-decoration: none;">Go Premium</a>
      </div>

      <div class="pricing-card" style="border: 2px solid var(--gold); box-shadow: 0 4px 12px rgba(245,158,11,0.05);">
        <div class="plan-name" style="font-size: 1.4rem; color: var(--gold);">Featured</div>
        <div class="price" style="color: var(--gold);">$79<span style="font-size:1rem; font-weight:400; color: var(--gray);">/mo</span></div>
        <p style="color: var(--gray); font-size: 0.9rem; margin-bottom: 16px;">Maximum exposure across the entire whatdentist directory.</p>
        <ul style="border-top: 1px solid #f1f5f9; padding-top: 16px;">
          <li>Everything in Premium</li>
          <li><strong>Unlimited cities listed</strong></li>
          <li><strong>Featured on Homepage</strong></li>
          <li>Trust Badge for your website</li>
          <li>Direct Lead Forwarding</li>
        </ul>
        <a href="/get-listed?plan=featured" class="btn btn-gold" style="display: block; margin-top: 24px; text-decoration: none;">Get Featured</a>
      </div>
    </div>

    <!-- Comparison Table -->
    <h2 style="text-align: center; margin-top: 60px; margin-bottom: 30px;">Plan Comparison Table</h2>
    <div style="overflow-x: auto; margin-bottom: 60px;">
      <table style="width: 100%; border-collapse: collapse; background: var(--white); border-radius: 12px; overflow: hidden; border: 1px solid #cbd5e1; font-size: 0.95rem; min-width: 600px;">
        <thead>
          <tr style="background: var(--dark); color: var(--white); text-align: left;">
            <th style="padding: 16px;">Features</th>
            <th style="padding: 16px; text-align: center;">Free ($0)</th>
            <th style="padding: 16px; text-align: center;">Verified ($29)</th>
            <th style="padding: 16px; text-align: center;">Premium ($49)</th>
            <th style="padding: 16px; text-align: center;">Featured ($79)</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid #e2e8f0;">
            <td style="padding: 16px; font-weight: 600;">Trust Badge Status</td>
            <td style="padding: 16px; text-align: center; color: var(--gray);">Unverified</td>
            <td style="padding: 16px; text-align: center; color: var(--primary); font-weight: 700;">Verified Seal</td>
            <td style="padding: 16px; text-align: center; color: var(--primary); font-weight: 700;">Verified Seal</td>
            <td style="padding: 16px; text-align: center; color: var(--primary); font-weight: 700;">Verified Seal</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
            <td style="padding: 16px; font-weight: 600;">City Listings</td>
            <td style="padding: 16px; text-align: center;">1 City</td>
            <td style="padding: 16px; text-align: center;">2 Cities</td>
            <td style="padding: 16px; text-align: center;">5 Cities</td>
            <td style="padding: 16px; text-align: center; font-weight: 700; color: var(--gold);">Unlimited</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0;">
            <td style="padding: 16px; font-weight: 600;">Photo Gallery</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓ (10 Photos)</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓ (Unlimited)</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓ (Unlimited)</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
            <td style="padding: 16px; font-weight: 600;">Before & After Photos</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0;">
            <td style="padding: 16px; font-weight: 600;">Pricing & Fee List</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
            <td style="padding: 16px; font-weight: 600;">Search Results Ranking</td>
            <td style="padding: 16px; text-align: center;">Standard</td>
            <td style="padding: 16px; text-align: center;">Elevated</td>
            <td style="padding: 16px; text-align: center; font-weight: 700; color: var(--primary);">High Priority</td>
            <td style="padding: 16px; text-align: center; font-weight: 700; color: var(--gold);">Top Ranking</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0;">
            <td style="padding: 16px; font-weight: 600;">Homepage Featuring</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓</td>
          </tr>
          <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
            <td style="padding: 16px; font-weight: 600;">Direct Lead Forwarding</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #ef4444;">❌</td>
            <td style="padding: 16px; text-align: center; color: #22c55e;">✓ (Real-time SMS/Email)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- FAQ Section -->
    <h2 style="text-align: center; margin-bottom: 40px;">Frequently Asked Questions</h2>
    <div style="max-width: 800px; margin: 0 auto 60px; display: flex; flex-direction: column; gap: 24px;">
      <div>
        <h3 style="color: var(--primary); font-size: 1.15rem; margin-bottom: 8px;">✓ How do I get the Verified badge?</h3>
        <p style="color: var(--gray);">To earn the Verified badge, you must submit your official Cédula Profesional (dental license number) and clinical specializations. Our administrative team audits this data against Mexican government and state dental registries to ensure clinical authenticity.</p>
      </div>
      <div>
        <h3 style="color: var(--primary); font-size: 1.15rem; margin-bottom: 8px;">✓ Can I upgrade or downgrade my plan at any time?</h3>
        <p style="color: var(--gray);">Yes. There are no long-term contracts on whatdentist.com.mx. You can upgrade, downgrade, or cancel your monthly plan directly from your clinic profile dashboard or by contacting support.</p>
      </div>
      <div>
        <h3 style="color: var(--primary); font-size: 1.15rem; margin-bottom: 8px;">✓ Are there long-term contracts or cancellation fees?</h3>
        <p style="color: var(--gray);">Absolutely not. All plans are billed on a month-to-month basis. You can cancel at any time, and you will not be billed for the subsequent month. There are no hidden setup fees or termination costs.</p>
      </div>
      <div>
        <h3 style="color: var(--primary); font-size: 1.15rem; margin-bottom: 8px;">✓ How do leads get delivered to my clinic?</h3>
        <p style="color: var(--gray);">For basic plans, patient submissions from your profile form are delivered to your registered email address. For Featured members, leads are instantly forwarded via real-time WhatsApp integration and SMS so your team can respond within minutes.</p>
      </div>
      <div>
        <h3 style="color: var(--primary); font-size: 1.15rem; margin-bottom: 8px;">✓ Do you charge commissions on patient treatments?</h3>
        <p style="color: var(--gray);">No. We believe in complete transparency. Unlike medical intermediary companies that demand 10-20% commission on patient treatments (which inflates patient costs), whatdentist charges a flat monthly directory listing fee. You keep 100% of your earnings, and patients get the lowest possible prices.</p>
      </div>
    </div>
  </div>
</section>
"""

    # Write Page 4
    with open('/app/sites/whatdentist/pricing.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Listing Plans & Pricing | whatdentist.com.mx",
            description="Find the perfect directory listing plan for your dental clinic in Mexico. Compare Free, Verified, Premium, and Featured options to grow your patient base.",
            canonical="https://whatdentist.com.mx/pricing",
            robots="index, follow",
            schema_tag=""
        ))
        f.write(header_html)
        f.write(pricing_content)
        f.write(footer_html)

    # 5. get-listed.html
    get_listed_content = """
<section class="hero" style="background: linear-gradient(135deg, #1e40af 0%, #06b6d4 100%);">
  <div class="container">
    <h1>Get Listed on whatdentist</h1>
    <p>Submit your clinic information to join Mexico's premier dental directory and reach thousands of international patients.</p>
  </div>
</section>

<section>
  <div class="container" style="max-width: 650px; background: var(--white); padding: 40px; border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
    <h2 style="margin-bottom: 8px; font-size: 1.6rem; color: var(--dark); text-align: center;">Register Your Practice</h2>
    <p style="color: var(--gray); font-size: 0.95rem; text-align: center; margin-bottom: 30px;">Fill out the form below. Our compliance and verification team will review your details within 24-48 business hours.</p>

    <form action="https://lyra-52971c5e.base44.app/functions/captureLead" method="POST">
      <!-- Hidden Fields -->
      <input type="hidden" name="sourceWebsite" value="whatdentist.com.mx">
      <input type="hidden" name="formType" value="dentist_registration">

      <div class="form-group">
        <label for="name">Dentist Full Name *</label>
        <input type="text" id="name" name="name" placeholder="e.g. Dr. Jane Doe" required>
      </div>

      <div class="form-group">
        <label for="email">Professional Email Address *</label>
        <input type="email" id="email" name="email" placeholder="e.g. contact@yourclinic.com" required>
      </div>

      <div class="form-group">
        <label for="clinicName">Clinic Name *</label>
        <input type="text" id="clinicName" name="clinicName" placeholder="e.g. Sani Dental Group" required>
      </div>

      <div class="form-group">
        <label for="city">Target City in Mexico *</label>
        <select id="city" name="city" required>
          <option value="" disabled selected>-- Select a City --</option>
          <option value="Los Algodones">Los Algodones (Molar City)</option>
          <option value="Tijuana">Tijuana</option>
          <option value="Cancun">Cancun</option>
          <option value="Monterrey">Monterrey</option>
          <option value="Puerto Vallarta">Puerto Vallarta</option>
          <option value="Mexico City">Mexico City</option>
          <option value="Other">Other City</option>
        </select>
      </div>

      <div class="form-group">
        <label for="specialties">Your Specialties *</label>
        <input type="text" id="specialties" name="specialties" placeholder="e.g. Dental Implants, Cosmetic Veneers, Endodontics" required>
      </div>

      <div class="form-group">
        <label for="phone">Phone Number (including Country Code) *</label>
        <input type="tel" id="phone" name="phone" placeholder="e.g. +1-928-374-4575 or +52 686..." required>
      </div>

      <div class="form-group">
        <label for="website">Clinic Website Address</label>
        <input type="url" id="website" name="website" placeholder="e.g. https://www.yourclinic.com">
      </div>

      <div class="form-group">
        <label for="plan">Desired Directory Plan *</label>
        <select id="plan" name="plan" required>
          <option value="" disabled selected>-- Choose a Plan --</option>
          <option value="Free ($0)">Free - Basic Listing ($0/mo)</option>
          <option value="Verified ($29)">Verified Seal - Enhanced Profile ($29/mo)</option>
          <option value="Premium ($49)">Premium - Featured Position ($49/mo)</option>
          <option value="Featured ($79)">Featured - Absolute Exposure ($79/mo)</option>
        </select>
      </div>

      <div style="margin: 24px 0 16px 0; font-size: 0.85rem; color: var(--gray);">
        <p>By submitting this form, you authorize whatdentist.com.mx to verify your medical licenses and professional details. We will contact you via email or phone to confirm activation.</p>
      </div>

      <button type="submit" class="btn-submit">Submit Registration Application</button>
    </form>
  </div>
</section>
"""

    # Write Page 5
    with open('/app/sites/whatdentist/get-listed.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Get Listed on whatdentist.com.mx | Free Dental Directory",
            description="Are you a dentist in Mexico? Register your dental clinic on whatdentist.com.mx to connect with US and Canadian dental tourism patients today.",
            canonical="https://whatdentist.com.mx/get-listed",
            robots="index, follow",
            schema_tag=""
        ))
        f.write(header_html)
        f.write(get_listed_content)
        f.write(footer_html)

    # 6. contact.html
    contact_content = """
<section class="hero" style="background: linear-gradient(135deg, #1e40af 0%, #06b6d4 100%);">
  <div class="container">
    <h1>Contact Us</h1>
    <p>Have questions about finding a dentist, verifying credentials, or listing your practice? Get in touch with our support team.</p>
  </div>
</section>

<section>
  <div class="container">
    <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 40px; align-items: start;">
      <!-- Contact Details -->
      <div style="background: var(--white); padding: 32px; border-radius: 12px; border: 1px solid #cbd5e1;">
        <h2 style="font-size: 1.5rem; color: var(--dark); margin-bottom: 24px;">Our Contact Information</h2>
        <p style="color: var(--gray); margin-bottom: 30px; font-size: 1rem;">We are committed to helping patients find safer, high-quality, and cost-effective dental treatment options across Mexico. Our help desk is available for patients and dentists alike.</p>
        
        <div style="display: flex; flex-direction: column; gap: 24px;">
          <div style="display: flex; gap: 16px; align-items: center;">
            <div style="font-size: 1.8rem; background: var(--light-gray); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">📞</div>
            <div>
              <h4 style="color: var(--dark); font-size: 1rem; margin-bottom: 2px;">Phone Number</h4>
              <p><a href="tel:+19283744575" style="font-weight: 700; font-size: 1.1rem; color: var(--primary);">928-374-4575</a></p>
            </div>
          </div>

          <div style="display: flex; gap: 16px; align-items: center;">
            <div style="font-size: 1.8rem; background: var(--light-gray); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">💬</div>
            <div>
              <h4 style="color: var(--dark); font-size: 1rem; margin-bottom: 2px;">WhatsApp Support</h4>
              <p><a href="https://wa.me/19283744575" style="font-weight: 700; font-size: 1.1rem; color: var(--green);">Chat with us on WhatsApp</a></p>
            </div>
          </div>

          <div style="display: flex; gap: 16px; align-items: center;">
            <div style="font-size: 1.8rem; background: var(--light-gray); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">✉️</div>
            <div>
              <h4 style="color: var(--dark); font-size: 1rem; margin-bottom: 2px;">Email Address</h4>
              <p><a href="mailto:irma@whatdentist.com.mx" style="font-weight: 700; font-size: 1.1rem; color: var(--primary);">irma@whatdentist.com.mx</a></p>
            </div>
          </div>
        </div>

        <div style="background: #f8fafc; padding: 20px; border-radius: 8px; margin-top: 40px; border-left: 4px solid var(--primary);">
          <h4 style="color: var(--dark); margin-bottom: 8px; font-size: 0.95rem; font-weight: 700;">Are you a patient?</h4>
          <p style="font-size: 0.85rem; color: var(--gray); line-height: 1.5;">Our referral advice is entirely free. Send us a copy of your local dental quote or diagnostic overview, and we can guide you to verified specialists in Mexico.</p>
        </div>
      </div>

      <!-- Contact Form -->
      <div style="background: var(--white); padding: 32px; border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
        <h2 style="font-size: 1.5rem; color: var(--dark); margin-bottom: 12px; text-align: center;">Send Us a Message</h2>
        <p style="color: var(--gray); text-align: center; margin-bottom: 24px; font-size: 0.95rem;">Have general feedback or an inquiry? Send a request below.</p>
        
        <form action="https://lyra-52971c5e.base44.app/functions/captureLead" method="POST">
          <input type="hidden" name="sourceWebsite" value="whatdentist.com.mx">
          <input type="hidden" name="formType" value="general_contact">

          <div class="form-group">
            <label for="name">Your Full Name *</label>
            <input type="text" id="name" name="name" placeholder="e.g. John Doe" required>
          </div>

          <div class="form-group">
            <label for="email">Email Address *</label>
            <input type="email" id="email" name="email" placeholder="e.g. john@example.com" required>
          </div>

          <div class="form-group">
            <label for="phone">Phone Number *</label>
            <input type="tel" id="phone" name="phone" placeholder="e.g. 928-374-4575" required>
          </div>

          <div class="form-group">
            <label for="message">Your Message or Inquiry *</label>
            <textarea id="message" name="message" rows="5" placeholder="Let us know how we can assist you..." required style="width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 1rem; background: var(--white); font-family: inherit; resize: vertical;"></textarea>
          </div>

          <button type="submit" class="btn-submit" style="margin-top: 12px;">Send Message</button>
        </form>
      </div>
    </div>
  </div>
</section>
"""

    # Write Page 6
    with open('/app/sites/whatdentist/contact.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Contact whatdentist.com.mx | Get in Touch",
            description="Contact whatdentist.com.mx for help finding certified dentists, verifying credentials, or inquiries about advertising and listing plans.",
            canonical="https://whatdentist.com.mx/contact",
            robots="index, follow",
            schema_tag=""
        ))
        f.write(header_html)
        f.write(contact_content)
        f.write(footer_html)

    # 7. about.html
    about_content = """
<section class="hero" style="background: linear-gradient(135deg, #1e40af 0%, #06b6d4 100%);">
  <div class="container">
    <h1>About whatdentist</h1>
    <p>Discover our mission to bring transparency, trust, and absolute safety to Mexico's dental tourism industry.</p>
  </div>
</section>

<section>
  <div class="container" style="max-width: 800px;">
    <h2>Our Mission & Credential Verification Standards</h2>
    <div style="font-size: 1.05rem; color: #334155; line-height: 1.8; display: flex; flex-direction: column; gap: 20px;">
      <p>
        Welcome to <strong>whatdentist.com.mx</strong>, Mexico's premier independent dental tourism directory. We are dedicated to connecting patients from the United States, Canada, and around the world with verified, high-quality, and affordable dental care in Mexico's top dental destinations, including Los Algodones, Tijuana, and Cancun.
      </p>
      <p>
        Our mission is simple: <strong>to bring transparency, safety, and trust</strong> to the dental tourism industry. We understand that deciding to travel abroad for dental work is a major decision that requires thorough research and peace of mind. While the cost savings in Mexico—often up to 70% less than in the US and Canada—are undeniable, finding a trustworthy, licensed, and skilled dentist can be a daunting process.
      </p>
      <p>
        That is where whatdentist comes in. Unlike other directories that allow any clinic to buy their way to the top of the search results, we employ a rigorous and multi-step verification process for our listed dentists. Our "Verified" badge is not just a marketing gimmick; it is a seal of clinical standards and professional integrity.
      </p>
      
      <h3 style="color: var(--primary); margin-top: 16px; font-size: 1.3rem;">Our Rigorous Verification Audit</h3>
      <p>When we verify a dentist, we perform a comprehensive audit containing the following steps:</p>
      <ul style="padding-left: 20px; display: flex; flex-direction: column; gap: 12px; margin-bottom: 8px;">
        <li>
          <strong>1. Official Licensing Check:</strong> We verify the dentist's official <em>Cédula Profesional</em> (Mexican professional license) and specialist licenses with the Mexican Secretariat of Public Education (SEP) to guarantee they are fully qualified to perform the procedures they advertise.
        </li>
        <li>
          <strong>2. Board Certification & Associations:</strong> We check and confirm active memberships and certifications with recognized national and international bodies, such as the Asociación Dental Mexicana (ADM), the American Dental Association (ADA), and state licensing boards.
        </li>
        <li>
          <strong>3. Clinic Inspection & Sterilization Protocols:</strong> We ensure that listed clinics follow strict international standards of sanitation and patient safety, including autoclave sterilization, advanced bio-hazard disposals, and state-of-the-art diagnostic imaging.
        </li>
        <li>
          <strong>4. Transparent Pricing Guarantee:</strong> We require verified dentists to publish clear, upfront price lists for their most common procedures so that patients never experience hidden fees or unexpected surcharges.
        </li>
        <li>
          <strong>5. Patient Review Verification:</strong> We screen patient reviews to ensure they represent real, authentic experiences from actual dental patients, weeding out fake testimonials.
        </li>
      </ul>

      <p>
        By eliminating the middlemen, whatdentist allows you to contact, consult, and book appointments directly with your chosen dentist, entirely commission-free. Our referral advice is entirely free of charge for patients, keeping your transaction straightforward and uninflated.
      </p>
      <p>
        We are here to help answer your questions and guide you toward a safer, happier, and more affordable smile. If you have any questions, you can contact us at <strong>928-374-4575</strong> or email <a href="mailto:irma@whatdentist.com.mx">irma@whatdentist.com.mx</a>. Thank you for choosing whatdentist.com.mx—your trusted partner in dental tourism.
      </p>
    </div>
  </div>
</section>

<div class="cta-bar">
  <div class="container">
    <h2>Ready to Find Your Vetted Dentist in Mexico?</h2>
    <p style="margin-top: 12px; font-size: 1.1rem;">Browse our listings, check certified pricing, and get in touch directly.</p>
    <a href="/los-algodones" class="btn btn-green">View Los Algodones Dentists →</a>
  </div>
</div>
"""

    # Write Page 7
    with open('/app/sites/whatdentist/about.html', 'w') as f:
        f.write(head_meta_template.format(
            title="About whatdentist.com.mx | Verified Dental Directory Mexico",
            description="Learn more about whatdentist.com.mx. Discover our mission of transparency and our rigorous professional audit process for verifying dentists in Mexico.",
            canonical="https://whatdentist.com.mx/about",
            robots="index, follow",
            schema_tag=""
        ))
        f.write(header_html)
        f.write(about_content)
        f.write(footer_html)

    # 8. 404.html
    not_found_content = """
<section style="min-height: 50vh; display: flex; align-items: center; text-align: center; background: var(--white);">
  <div class="container" style="max-width: 600px; padding: 40px 20px;">
    <span style="font-size: 5rem; display: block; margin-bottom: 24px;">🔍</span>
    <h1 style="font-size: 3rem; color: var(--primary); margin-bottom: 12px;">404 — Page Not Found</h1>
    <p style="color: var(--gray); font-size: 1.2rem; margin-bottom: 30px;">The page you are looking for does not exist or has been moved. Use the navigation above or the links below to return to our verified directories.</p>
    
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px;">
      <a href="/" class="btn btn-primary" style="padding: 12px 24px;">🏠 Return Home</a>
      <a href="/los-algodones" class="btn btn-green" style="padding: 12px 24px;">📍 Los Algodones</a>
      <a href="/pricing" class="btn btn-gold" style="padding: 12px 24px; color: white;">💰 Directory Pricing</a>
    </div>
    
    <div style="margin-top: 40px; border-top: 1px solid #f1f5f9; padding-top: 24px;">
      <p style="font-size: 0.95rem; color: var(--gray);">Need assistance? Contact our team directly via WhatsApp or phone at <a href="tel:+19283744575" style="font-weight: 700;">928-374-4575</a>.</p>
    </div>
  </div>
</section>
"""

    # Write Page 8
    with open('/app/sites/whatdentist/404.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Page Not Found | whatdentist.com.mx",
            description="Error 404 — The page you requested could not be found. Return to whatdentist.com.mx, Mexico's leading verified dental directory.",
            canonical="https://whatdentist.com.mx/404",
            robots="noindex, follow",
            schema_tag=""
        ))
        f.write(header_html)
        f.write(not_found_content)
        f.write(footer_html)

    # 9. dentist/dr-jose-moguel.html
    jose_moguel_schema = """<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Dentist",
    "name": "Dr. José Moguel",
    "image": "https://media.base44.com/images/public/6a5301f7d191f37052971c5e/7483864c6_Dr-Jose-Moguel-Dental-Implant-Expertise-in-Mexico-los-algodones.webp",
    "telephone": "+1-928-374-4575",
    "priceRange": "$$",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Los Algodones",
      "addressRegion": "Baja California",
      "addressCountry": "MX"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "5.0",
      "reviewCount": "847"
    }
  }
  </script>"""

    jose_moguel_content = """
<section style="background: var(--white); border-bottom: 1px solid #e2e8f0; padding: 24px 0;">
  <div class="container" style="font-size: 0.9rem; color: var(--gray); margin-bottom: 16px;">
    <a href="/">Home</a> &raquo; <a href="/los-algodones">Los Algodones</a> &raquo; <strong style="color: var(--dark);">Dr. José Moguel</strong>
  </div>
  <div class="container" style="display: grid; grid-template-columns: 240px 1fr; gap: 32px; align-items: center;">
    <img src="https://media.base44.com/images/public/6a5301f7d191f37052971c5e/7483864c6_Dr-Jose-Moguel-Dental-Implant-Expertise-in-Mexico-los-algodones.webp" alt="Dr. José Moguel — Dental Implant Specialist" style="width: 100%; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">
    <div>
      <div style="display: flex; gap: 8px; margin-bottom: 12px;">
        <span class="badge badge-featured" style="margin:0;">⭐ Featured Partner</span>
        <span class="badge badge-verified" style="margin:0;">✓ Verified Surgeon</span>
      </div>
      <h1 style="font-size: 2.2rem; color: var(--dark); margin-bottom: 8px; line-height: 1.2;">Dr. José Moguel — Dental Implant Specialist</h1>
      <p class="specialty" style="font-size: 1.15rem; color: var(--primary); font-weight: 600; margin-bottom: 8px;">Dental Implants • All-on-4 • 3-ON-8™ • Periodontics</p>
      <p style="font-size: 1.1rem; font-weight: 700; color: var(--gold); margin-bottom: 8px;">⭐ 5.0 (847 Verified Patient Reviews)</p>
      <p style="font-size: 1rem; color: var(--gray);">📍 Avenida B, Los Algodones, Baja California, Mexico</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="display: grid; grid-template-columns: 2fr 1.1fr; gap: 40px; align-items: start;">
      
      <!-- Profile Details -->
      <div>
        <h2>Professional Biography</h2>
        <div style="font-size: 1.05rem; color: #334155; line-height: 1.7; display: flex; flex-direction: column; gap: 16px; margin-bottom: 40px;">
          <p>
            <strong>Dr. José Moguel</strong> is a highly distinguished dental implant surgeon and periodontist practicing in Los Algodones, Mexico. With over 15 years of clinical expertise, Dr. Moguel has successfully placed thousands of dental implants, restoring health, aesthetics, and chewing functionality to patients traveling from all 50 US states and every Canadian province.
          </p>
          <p>
            Dr. Moguel specializes in complex, high-complexity implant placements, full-mouth reconstructions, sinus lifts, bone grafting, and periodontics. He is a certified practitioner of advanced full-arch restorations, specializing in standard <strong>All-on-4</strong> and the advanced, high-stability <strong>3-ON-8™</strong> protocol, which provides unparalleled structural support for fixed porcelain bridges.
          </p>
          <p>
            His dental practice employs state-of-the-art diagnostics, incorporating high-resolution 3D Cone-Beam CT (CBCT) scanning and laser dentistry. Dr. Moguel operates in a modern, ultra-sanitized environment following strict ADA and OSHA sterilization guidelines, ensuring patient safety and clinical success at every stage of the surgical process.
          </p>
        </div>

        <h2>Specialties & Clinical Procedures</h2>
        <ul style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; list-style: none; font-size: 1rem; color: #334155; margin-bottom: 40px;">
          <li style="display:flex; align-items:center; gap:8px;">✔️ Single Dental Implants (Titanium)</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ All-on-4® Full-Arch Restorations</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Specialized 3-ON-8™ Protocol</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Periodontal Surgery & Therapy</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Bone Grafting & Sinus Lifts</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Zirconia & Porcelain Crowns</li>
        </ul>

        <h2>Board Certifications & Academic Credentials</h2>
        <div style="font-size: 1rem; color: #334155; line-height: 1.7; display: flex; flex-direction: column; gap: 12px; margin-bottom: 40px; background: var(--white); padding: 24px; border-radius: 12px; border: 1px solid #cbd5e1;">
          <p>🎓 <strong>Dental Surgery Degree (DDS)</strong> — Universidad Autónoma de Baja California (UABC).</p>
          <p>🎓 <strong>Master's in Implantology & Periodontics</strong> — Recognized by the Secretariat of Public Education (SEP) with active Cédula Profesional Specialist Licensure.</p>
          <p>💼 <strong>Active Member</strong> of the Asociación Dental Mexicana (ADM).</p>
          <p>💼 <strong>International Member</strong> of the International Congress of Oral Implantologists (ICOI).</p>
        </div>

        <h2>Transparent Treatment Pricing</h2>
        <p style="color: var(--gray); margin-bottom: 16px; font-size: 0.95rem;">Dr. José Moguel is committed to complete pricing transparency. See standard surgical fees below:</p>
        <table style="width: 100%; border-collapse: collapse; background: var(--white); border-radius: 12px; overflow: hidden; border: 1px solid #cbd5e1; font-size: 0.95rem; margin-bottom: 40px;">
          <thead>
            <tr style="background: var(--dark); color: white; text-align: left;">
              <th style="padding: 12px 16px;">Treatment / Procedure</th>
              <th style="padding: 12px 16px; text-align: right;">Average US Price</th>
              <th style="padding: 12px 16px; text-align: right; color: #10b981;">Dr. Moguel Price</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid #e2e8f0;">
              <td style="padding: 12px 16px; font-weight: 600;">Standard Titanium Dental Implant</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$4,000</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$800</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
              <td style="padding: 12px 16px; font-weight: 600;">Porcelain-Fused-to-Metal Crown</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$1,100</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$350</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0;">
              <td style="padding: 12px 16px; font-weight: 600;">High-Aesthetic Zirconia Crown</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$1,400</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$450</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
              <td style="padding: 12px 16px; font-weight: 600;">All-on-4® Full Arch (Fixed Acrylic)</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$24,000</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$8,500</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0;">
              <td style="padding: 12px 16px; font-weight: 600;">Bone Grafting (per unit)</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$800</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$400</td>
            </tr>
            <tr style="background: #f8fafc;">
              <td style="padding: 12px 16px; font-weight: 600;">Standard Sinus Lift</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$2,500</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$950</td>
            </tr>
          </tbody>
        </table>

        <h2>Verified Patient Reviews</h2>
        <div style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 40px;">
          <div style="background: var(--white); padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0;">
            <p style="color: var(--gold); font-weight: 700; margin-bottom: 6px;">⭐⭐⭐⭐⭐ (5/5)</p>
            <p style="font-style: italic; color: #334155;">"I needed a full All-on-4 on my upper arch. Quotes in Salt Lake City were around $26,000. I traveled to Los Algodones and Dr. Moguel completed my treatment for $8,500. The clinic was modern, the team was incredibly professional, and my implants feel completely natural."</p>
            <p style="font-size: 0.85rem; color: var(--gray); margin-top: 8px; font-weight: 600;">— David R., Salt Lake City, UT • March 2026</p>
          </div>
          <div style="background: var(--white); padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0;">
            <p style="color: var(--gold); font-weight: 700; margin-bottom: 6px;">⭐⭐⭐⭐⭐ (5/5)</p>
            <p style="font-style: italic; color: #334155;">"Highly recommend Dr. Moguel! He is incredibly reassuring, explains everything step-by-step, and has very steady hands. I got two implants and bone grafting. The pain was minimal and the savings were immense."</p>
            <p style="font-size: 0.85rem; color: var(--gray); margin-top: 8px; font-weight: 600;">— Martha S., Yuma, AZ • June 2026</p>
          </div>
        </div>
      </div>

      <!-- Contact / Lead Gen Form -->
      <div style="background: var(--white); padding: 28px; border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.02); position: sticky; top: 100px;">
        <h3 style="margin-bottom: 8px; color: var(--primary); font-size: 1.3rem;">Request Consultation</h3>
        <p style="color: var(--gray); font-size: 0.9rem; margin-bottom: 20px;">Connect directly with Dr. José Moguel's office. Free consultation request.</p>
        
        <form action="https://lyra-52971c5e.base44.app/functions/captureLead" method="POST">
          <input type="hidden" name="sourceWebsite" value="whatdentist.com.mx">
          <input type="hidden" name="dentistName" value="Dr. José Moguel">
          <input type="hidden" name="formType" value="patient_consultation">

          <div class="form-group">
            <label for="name" style="font-size: 0.9rem;">Your Full Name *</label>
            <input type="text" id="name" name="name" placeholder="John Doe" required style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="email" style="font-size: 0.9rem;">Email Address *</label>
            <input type="email" id="email" name="email" placeholder="john@example.com" required style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="phone" style="font-size: 0.9rem;">Phone Number *</label>
            <input type="tel" id="phone" name="phone" placeholder="e.g. 928-374-4575" required style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="desiredDate" style="font-size: 0.9rem;">Desired Appointment Date</label>
            <input type="date" id="desiredDate" name="desiredDate" style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="message" style="font-size: 0.9rem;">Describe Your Needs / Procedure *</label>
            <textarea id="message" name="message" rows="4" placeholder="e.g. Interested in All-on-4 Upper Arch..." required style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:8px; font-family:inherit; font-size: 0.95rem;"></textarea>
          </div>

          <button type="submit" class="btn-submit" style="padding: 12px 20px; font-size: 1rem;">Send Consultation Request</button>
        </form>

        <div style="margin-top: 20px; border-top: 1px solid #f1f5f9; padding-top: 16px; text-align: center;">
          <p style="font-size: 0.85rem; color: var(--gray); margin-bottom: 8px;">Prefer to call or text?</p>
          <a href="https://wa.me/19283744575" class="btn btn-green" style="display: block; font-size: 0.9rem;">💬 WhatsApp: 928-374-4575</a>
        </div>
      </div>

    </div>
  </div>
</section>
"""

    # Write Page 9
    with open('/app/sites/whatdentist/dentist/dr-jose-moguel.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Dr. José Moguel — Dental Implants Los Algodones | 5.0★ | 847 Reviews",
            description="View Dr. José Moguel's profile on whatdentist.com.mx. Vetted dental implant specialist in Los Algodones, Mexico. Read patient reviews, compare pricing, and request free consultation.",
            canonical="https://whatdentist.com.mx/dentist/dr-jose-moguel",
            robots="index, follow",
            schema_tag=jose_moguel_schema
        ))
        f.write(header_html)
        f.write(jose_moguel_content)
        f.write(footer_html)

    # 10. dentist/dr-jonatan-sevilla.html
    jonatan_sevilla_schema = """<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Dentist",
    "name": "Dr. Jonatan Sevilla",
    "telephone": "+1-928-374-4575",
    "priceRange": "$$",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Los Algodones",
      "addressRegion": "Baja California",
      "addressCountry": "MX"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "312"
    }
  }
  </script>"""

    jonatan_sevilla_content = """
<section style="background: var(--white); border-bottom: 1px solid #e2e8f0; padding: 24px 0;">
  <div class="container" style="font-size: 0.9rem; color: var(--gray); margin-bottom: 16px;">
    <a href="/">Home</a> &raquo; <a href="/los-algodones">Los Algodones</a> &raquo; <strong style="color: var(--dark);">Dr. Jonatan Sevilla</strong>
  </div>
  <div class="container" style="display: grid; grid-template-columns: 240px 1fr; gap: 32px; align-items: center;">
    <div style="width: 100%; aspect-ratio: 1; background: linear-gradient(135deg, #2563eb, #06b6d4); display: flex; align-items: center; justify-content: center; color: white; font-size: 5rem; font-weight: 800; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">DS</div>
    <div>
      <div style="display: flex; gap: 8px; margin-bottom: 12px;">
        <span class="badge badge-featured" style="margin:0;">⭐ Featured Partner</span>
        <span class="badge badge-pending" style="margin:0;">⏳ Pending Verification Audit</span>
      </div>
      <h1 style="font-size: 2.2rem; color: var(--dark); margin-bottom: 8px; line-height: 1.2;">Dr. Jonatan Sevilla — Cosmetic Dentistry</h1>
      <p class="specialty" style="font-size: 1.15rem; color: var(--primary); font-weight: 600; margin-bottom: 8px;">Veneers • Crowns • Smile Makeovers • Cosmetic Dentistry</p>
      <p style="font-size: 1.1rem; font-weight: 700; color: var(--gold); margin-bottom: 8px;">⭐ 4.9 (312 Patient Reviews)</p>
      <p style="font-size: 1rem; color: var(--gray);">📍 Calle 2a, Los Algodones, Baja California, Mexico</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="display: grid; grid-template-columns: 2fr 1.1fr; gap: 40px; align-items: start;">
      
      <!-- Profile Details -->
      <div>
        <h2>Professional Biography</h2>
        <div style="font-size: 1.05rem; color: #334155; line-height: 1.7; display: flex; flex-direction: column; gap: 16px; margin-bottom: 40px;">
          <p>
            <strong>Dr. Jonatan Sevilla</strong> is a leading aesthetic and cosmetic dentist in Los Algodones, Mexico, recognized for designing stunning, custom smiles. Dr. Sevilla specializes in full mouth reconstructions, advanced smile design, custom porcelain veneers, Zirconia crowns, and state-of-the-art dental bonding.
          </p>
          <p>
            Having completed extensive post-graduate training in cosmetic rehabilitation and clinical occlusion, Dr. Sevilla focuses on blending structural health with beautiful, radiant aesthetics. His approach centers around meticulous shade matching and smile line personalization, ensuring that every crown or veneer enhances the patient's natural facial structure.
          </p>
          <p>
            Dr. Sevilla uses top-tier, bio-compatible dental materials sourced from premier manufacturers in the US and Germany. His clinic partners with premium local dental labs to ensure rapid turnaround times for crowns and veneers, allowing patients on tight travel timelines to complete entire mouth restorations in just a few days.
          </p>
        </div>

        <h2>Specialties & Cosmetic Treatments</h2>
        <ul style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; list-style: none; font-size: 1rem; color: #334155; margin-bottom: 40px;">
          <li style="display:flex; align-items:center; gap:8px;">✔️ Custom Porcelain Veneers</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ High-Translucency Zirconia Crowns</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Full-Mouth Cosmetic Smile Makeovers</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Inlays, Onlays, and Dental Bonding</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Laser Teeth Whitening</li>
          <li style="display:flex; align-items:center; gap:8px;">✔️ Porcelain-fused-to-metal (PFM) Crowns</li>
        </ul>

        <h2>Credentials & Education</h2>
        <div style="font-size: 1rem; color: #334155; line-height: 1.7; display: flex; flex-direction: column; gap: 12px; margin-bottom: 40px; background: var(--white); padding: 24px; border-radius: 12px; border: 1px solid #cbd5e1;">
          <p>🎓 <strong>Dental Surgeon Degree (DDS)</strong> — Recognized with honors.</p>
          <p>🎓 <strong>Specialization in Aesthetic Dental Rehabilitation</strong> — Advanced certifications in aesthetic dentistry.</p>
          <p>💼 <strong>Active Member</strong> of national aesthetic dental circles in Mexico.</p>
        </div>

        <h2>Cosmetic Procedure Pricing</h2>
        <p style="color: var(--gray); margin-bottom: 16px; font-size: 0.95rem;">Review Dr. Sevilla's standard aesthetic dental fees below:</p>
        <table style="width: 100%; border-collapse: collapse; background: var(--white); border-radius: 12px; overflow: hidden; border: 1px solid #cbd5e1; font-size: 0.95rem; margin-bottom: 40px;">
          <thead>
            <tr style="background: var(--dark); color: white; text-align: left;">
              <th style="padding: 12px 16px;">Treatment / Procedure</th>
              <th style="padding: 12px 16px; text-align: right;">Average US Price</th>
              <th style="padding: 12px 16px; text-align: right; color: #10b981;">Dr. Sevilla Price</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid #e2e8f0;">
              <td style="padding: 12px 16px; font-weight: 600;">High-Grade Porcelain Veneer (per unit)</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$1,600</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$450</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
              <td style="padding: 12px 16px; font-weight: 600;">High-Translucency Zirconia Crown</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$1,400</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$450</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0;">
              <td style="padding: 12px 16px; font-weight: 600;">Porcelain-Fused-to-Metal Crown</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$1,100</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$350</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
              <td style="padding: 12px 16px; font-weight: 600;">Zoom! Laser Teeth Whitening</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$650</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$200</td>
            </tr>
            <tr style="border-bottom: 1px solid #e2e8f0;">
              <td style="padding: 12px 16px; font-weight: 600;">Composite Dental Bonding</td>
              <td style="padding: 12px 16px; text-align: right; text-decoration: line-through; color: var(--gray);">$450</td>
              <td style="padding: 12px 16px; text-align: right; font-weight: 700; color: #10b981;">$150</td>
            </tr>
          </tbody>
        </table>

        <h2>Patient Reviews</h2>
        <div style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 40px;">
          <div style="background: var(--white); padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0;">
            <p style="color: var(--gold); font-weight: 700; margin-bottom: 6px;">⭐⭐⭐⭐⭐ (5/5)</p>
            <p style="font-style: italic; color: #334155;">"I went to Dr. Sevilla for a set of 8 porcelain veneers on my top teeth. They look absolutely gorgeous—so clean and bright, but natural in shape. I was back in California in 4 days. Unbelievable savings."</p>
            <p style="font-size: 0.85rem; color: var(--gray); margin-top: 8px; font-weight: 600;">— Jessica L., Palm Springs, CA • January 2026</p>
          </div>
          <div style="background: var(--white); padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0;">
            <p style="color: var(--gold); font-weight: 700; margin-bottom: 6px;">⭐⭐⭐⭐⭐ (5/5)</p>
            <p style="font-style: italic; color: #334155;">"Dr. Sevilla and his team are total artists. I had heavily stained teeth and some chips. They did zirconia crowns and a whitening. My smile is completely transformed."</p>
            <p style="font-size: 0.85rem; color: var(--gray); margin-top: 8px; font-weight: 600;">— Robert M., Las Vegas, NV • May 2026</p>
          </div>
        </div>
      </div>

      <!-- Contact Form -->
      <div style="background: var(--white); padding: 28px; border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.02); position: sticky; top: 100px;">
        <h3 style="margin-bottom: 8px; color: var(--primary); font-size: 1.3rem;">Request Consultation</h3>
        <p style="color: var(--gray); font-size: 0.9rem; margin-bottom: 20px;">Connect directly with Dr. Jonatan Sevilla's office. Free consultation request.</p>
        
        <form action="https://lyra-52971c5e.base44.app/functions/captureLead" method="POST">
          <input type="hidden" name="sourceWebsite" value="whatdentist.com.mx">
          <input type="hidden" name="dentistName" value="Dr. Jonatan Sevilla">
          <input type="hidden" name="formType" value="patient_consultation">

          <div class="form-group">
            <label for="name" style="font-size: 0.9rem;">Your Full Name *</label>
            <input type="text" id="name" name="name" placeholder="John Doe" required style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="email" style="font-size: 0.9rem;">Email Address *</label>
            <input type="email" id="email" name="email" placeholder="john@example.com" required style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="phone" style="font-size: 0.9rem;">Phone Number *</label>
            <input type="tel" id="phone" name="phone" placeholder="e.g. 928-374-4575" required style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="desiredDate" style="font-size: 0.9rem;">Desired Appointment Date</label>
            <input type="date" id="desiredDate" name="desiredDate" style="padding: 10px;">
          </div>

          <div class="form-group">
            <label for="message" style="font-size: 0.9rem;">Describe Your Needs / Procedure *</label>
            <textarea id="message" name="message" rows="4" placeholder="e.g. Interested in porcelain veneers..." required style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:8px; font-family:inherit; font-size: 0.95rem;"></textarea>
          </div>

          <button type="submit" class="btn-submit" style="padding: 12px 20px; font-size: 1rem;">Send Consultation Request</button>
        </form>

        <div style="margin-top: 20px; border-top: 1px solid #f1f5f9; padding-top: 16px; text-align: center;">
          <p style="font-size: 0.85rem; color: var(--gray); margin-bottom: 8px;">Prefer to call or text?</p>
          <a href="https://wa.me/19283744575" class="btn btn-green" style="display: block; font-size: 0.9rem;">💬 WhatsApp: 928-374-4575</a>
        </div>
      </div>

    </div>
  </div>
</section>
"""

    # Write Page 10
    with open('/app/sites/whatdentist/dentist/dr-jonatan-sevilla.html', 'w') as f:
        f.write(head_meta_template.format(
            title="Dr. Jonatan Sevilla — Cosmetic Dentistry Los Algodones | 4.9★",
            description="View Dr. Jonatan Sevilla's profile on whatdentist.com.mx. Dedicated cosmetic dentist in Los Algodones, Mexico. Read patient reviews, compare pricing, and request free consultation.",
            canonical="https://whatdentist.com.mx/dentist/dr-jonatan-sevilla",
            robots="index, follow",
            schema_tag=jonatan_sevilla_schema
        ))
        f.write(header_html)
        f.write(jonatan_sevilla_content)
        f.write(footer_html)

    print("Successfully generated all 10 files!")

if __name__ == "__main__":
    generate_pages()
