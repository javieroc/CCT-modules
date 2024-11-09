## CCT College Dublin

|                        |                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------|
| **Module Title:**      | Security Frameworks and Compliance                                                           |
| **Assessment Title:**  | Cybersecurity Standards Evaluation and Recommendations for Enhancing Organizational Security |
| **Lecturer Name:**     | Dr. Naila Aslam                                                                              |
| **Student Full Name:** | Javier Alfonso Ocampo                                                                        |
| **Student Number:**    | 2024328                                                                                      |


### Task 1: Evaluate Current Cybersecurity Frameworks

- **SOC 2**: Ensures the organization’s data security practices meet specific standards necessary for protecting sensitive information. This framework is valuable for the healthcare organization because it rigorously assesses and verifies the effectiveness of internal controls across critical areas such as security, confidentiality, and privacy. By following SOC 2, the organization can demonstrate a commitment to data protection, reduce the risks associated with unauthorized access to patient records, and enhance trust among patients, staff, and stakeholders by validating the safety and integrity of its systems.

  - **Strength**: SOC 2 is particularly strong at verifying and validating an organisation’s internal controls around data protection. By focusing on security, confidentiality, privacy, processing integrity, and availability, SOC 2 helps ensure that sensitive data is well-protected against unauthorised access.
  - **Limitation**: SOC 2 is not a real-time framework; it involves periodic audits, meaning it may miss dynamic or emerging threats between assessments. It relies heavily on documentation and process adherence, which might not fully address new, sophisticated cyber threats that evolve rapidly.

- **GDPR**: Focuses on safeguarding personal data and upholding privacy rights of individuals, which is essential in healthcare given the sensitivity of patient information. GDPR compliance requires the organization to handle, store, and process data responsibly and securely, with strict patient consent protocols. This compliance reduces the likelihood of data breaches, strengthens patient privacy protections, and helps the organization avoid significant financial penalties and legal repercussions associated with data misuse or failure to adhere to privacy standards. GDPR also enhances transparency, empowering patients with control over their personal data.

  - **Strength**: GDPR provides a high level of protection for personal data through strict requirements around data consent, transparency, and privacy rights. This is especially strong for healthcare organisations, as it grants patients control over their personal data, increasing trust and accountability.
  - **Limitation**: While GDPR provides robust privacy protections, it can be challenging to implement consistently across different systems, especially if these systems span multiple regions or countries with varying laws. Additionally, GDPR doesn’t specify technical controls, so organisations may face challenges in determining the exact cybersecurity measures required for compliance.

- **NIST**: Provides a comprehensive framework for managing cybersecurity risks through structured guidelines and robust security controls. For the healthcare organization, implementing NIST is critical for systematically identifying potential risks, protecting systems, detecting security threats, and ensuring effective response and recovery in case of incidents. This framework strengthens the organization’s resilience, which is particularly crucial in healthcare due to the sensitive nature of patient data. Adopting NIST controls helps maintain patient trust, ensures operational continuity, and reduces vulnerabilities that could lead to breaches or unauthorized access.

  - **Strength**: NIST provides comprehensive and flexible guidelines for identifying and managing cybersecurity risks. It’s particularly effective in guiding organisations through a structured risk assessment and establishing detailed security controls that can be tailored to specific needs, making it ideal for healthcare’s varied data environments.
  - **Limitation**: NIST, being a voluntary framework, may not be as enforceable as GDPR or SOC 2, particularly for organisations outside of the U.S. Furthermore, while NIST is thorough, it can be resource-intensive to implement fully, which may be a challenge for smaller organisations with limited budgets or cybersecurity resources.


### Task 2: Identify Vulnerabilities in Current Practices

1. **Lack of Network Segmentation**: Without proper network segmentation, an attacker gaining access to one part of the system could potentially move freely across the entire network, reaching sensitive patient data and increasing the likelihood of a data breach. This vulnerability violates **SOC 2** and **GDPR** standards, as both require robust controls to limit data access. SOC 2 emphasises securing data through defined access boundaries, and GDPR mandates controlled access to protect privacy. Furthermore, **NIST** recommends network segmentation to limit the impact of potential threats, so a lack of segmentation falls short of its guidelines for effective threat containment.

2. **Insufficient Incident Response Planning**: Without a tested incident response plan, the organisation may not be able to detect or respond to a breach quickly, leaving patient data exposed for longer periods. This failure impacts compliance with **SOC 2**, which requires procedures for rapid breach detection and containment, and **GDPR**, which mandates timely breach notifications. A delayed response can result in higher fines and reputational damage under GDPR. The **NIST framework** also highlights incident response as a key part of security best practices, so insufficient planning in this area means the organisation isn’t fully aligning with its guidance for risk management and containment.


### Task 3: Recommendations for Improvement

1. **Implement Network Segmentation**: To address the lack of network segmentation, the organisation should divide its network into isolated sections based on data sensitivity and user roles. This measure would comply with **SOC 2** by strengthening internal access controls and safeguarding patient data. For **GDPR**, it helps enforce data minimisation by restricting access only to areas necessary for specific roles, supporting privacy requirements. Network segmentation aligns with **NIST** guidelines on limiting lateral movement, which can contain and isolate potential breaches. This added layer of security makes it far more challenging for unauthorised users or attackers to move freely across systems, reducing the likelihood of widespread data exposure.

2. **Develop and Regularly Test an Incident Response Plan**: Creating and testing a robust incident response plan would enhance the organisation’s ability to respond swiftly to potential breaches, ensuring quick detection, containment, and recovery. This aligns with **SOC 2**, which calls for thorough incident response protocols to reduce data exposure in case of a breach. For **GDPR**, a tested response plan ensures timely breach notifications, maintaining compliance with its notification requirements. Following **NIST** recommendations, which emphasise response and recovery as key pillars, this practice reduces the impact of breaches on patient data and allows for efficient restoration of services, ultimately improving resilience and safeguarding compliance.
