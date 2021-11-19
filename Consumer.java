package capstone1;

public class Consumer {
	/**
	 * These are the attributes for the consumer object.
	 */
	private String name;
	private String telephone;
	private String email;
	private String physicalAddress;
	private double amountPaid;
	
	// constructor
	/**
	 * 
	 * @param name of the consumer
	 * @param telephone of the consumer
	 * @param email of the consumer
	 * @param physicalAddress of the consumer
	 */
	public Consumer(String name, String telephone, String email, String physicalAddress, double amountPaid) {
		this.name = name;
		this.telephone = telephone;
		this.email = email;
		this.physicalAddress = physicalAddress;
		this.amountPaid = amountPaid;
	}

	
	public String getName() {
		return name;
	}
			
	public String getTelephone() {
		return telephone;
	}
	
	/**
	 * this is a setter which we will call from the main class.
	 * @param telephone to change/update the telephone
	 */
	public void setTelephone(String telephone) {
		this.telephone = telephone;
	}

	public String getEmail() {
		return email;
	}

	public String getPhysicalAddress() {
		return physicalAddress;
	}

	public double getAmountPaid() {
		return amountPaid;
	}
	
	/**
	 * this is the setter that we will call in the main class
	 * @param amountPaid to change/update the amount paid by the client
	 * @return 
	 */
	
	public void setAmountPaid(double amountPaid) {
		this.amountPaid = amountPaid;
		
	}
	/**
	 * this toString method will call out the variables from the main class
	 */

	public String toString() {
		String objectString = "Name: " + name +
			"\nTelephone: " + telephone +
			"\nEmail: " + email +
			"\nPhysical Address: " + physicalAddress +
			"\nAmount paid: " + amountPaid + "\n";
		
		return objectString;	
}

}
 