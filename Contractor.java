package capstone1;

public class Contractor {
	//Attributes for the Contractor object.
	private String name;
	private String telephone;
	private String email;
	private String physicalAddress;
	
	// constructor
	/**
	 * 
	 * @param contractor's name
	 * @param contractor's telephone
	 * @param contractor's email
	 * @param contractor's physicalAddress
	 */
	public Contractor(String name, String telephone, String email, String physicalAddress) {
		this.name = name;
		this.telephone = telephone;
		this.email = email;
		this.physicalAddress = physicalAddress;
	}

	public String getName() {
		return name;
	}

	public String getTelephone() {
		return telephone;
	}
	//This setter will be called from the main class,
	//we will use it to change the contractor's contact.
	
	public void setTelephone(String telephone) {
		this.telephone = telephone;
	}
	

	public String getEmail() {
		return email;
	}
	
	//This setter will be called from the main class,
	//we will use it to change the contractor's email.
	
	public void setEmail(String email) {
		this.email =email;
	}


	public String getPhysicalAddress() {
		return physicalAddress;
	}

	/**
	 * this toString method will call out the variables from the main class
	 */
	
	public String toString() {
		String objectString = "Name: " + name +
			"\nTelephone: " + telephone +
			"\nEmail: " + email +
			"\nPhysical Address: " + physicalAddress + "\n";
		
		return objectString;
}
	
}
