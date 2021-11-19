package capstone1;

public class Architect {
	//Attributes for the Architect object
	private String name;
	private String telephone;
	private String email;
	private String physicalAddress;
	
	/**
	 * this is the constructor for the Architect
	 * @param architect's name
	 * @param arcitect's telephone
	 * @param architect's email
	 * @param arcitect's physicalAddress
	 */
	
	public Architect(String name, String telephone, String email, String physicalAddress) {
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

	public String getEmail() {
		return email;
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