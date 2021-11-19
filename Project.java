package capstone1;

public class Project {
	//Attributes
	private int projectNumber;
	private String projectName;
	private String buildingType;
	private String physicalAddress;
	private int erfNumber;
	private String deadline;
	private double amountDue;
	private double amountReceived;
	public Consumer person;
	public Architect person2;
	public Contractor person3;
	
	// constructor
	/**
	 * this is the constructor for the project class
	 * @param the projectNumber for the project class
	 * @param the projectName for the project class
	 * @param the buildingType for the project class
	 * @param the physicalAddress for the project class
	 * @param the erfNumber for the project class
	 * @param the deadline for the project
	 * @param the amountDue for the project
	 * @param the person variable is the consumer class
	 * @param the person2 variable is the Architect class
	 * @param the person3 variable is the Contractor class
	 */
	
	public Project(int projectNumber, String projectName, String buildingType, 
			String physicalAddress, int erfNumber, String deadline, double amountDue , 
			Consumer person, Architect person2, Contractor person3) {
		this.projectNumber = projectNumber;
		this.projectName = projectName;
		this.buildingType = buildingType;
		this.physicalAddress = physicalAddress;
		this.erfNumber = erfNumber;
		this.deadline = deadline;
		this.amountDue = amountDue;
		amountReceived = 0;
		this.person = person;
		this.person2 = person2;
		this.person3 = person3;

	}

	public double getAmountDue() {
		return amountDue - amountReceived;
	}
	
	/**
	 * we will call this setter from the main class. 
	 * @param we will use Due to update amount due.
	 */
	public void setAmountDue(double Due) {
		this.amountDue = Due;
	}

	public double getAmountReceived() {
		return amountReceived;
	}

	/**
	 * we will call this setter in the main class  
	 * @param we will use it to update the amountRecieved 
	 */
	
	public void setAmountReceived(double received) {
		this.amountReceived = received;
	}

	public String getDeadline() {
		return deadline;
	}
	/**
	 * we will call the setter in the main class
	 * @param we will use it to update the deadline
	 */
	public void setDeadline(String deadline) {
		this.deadline = deadline;
	}

	public int getProjectNumber() {
		return projectNumber;
	}

	public String getProjectName() {
		return projectName;
	}

	public String getBuildingType() {
		return buildingType;
	}

	public String getPhysicalAddress() {
		return physicalAddress;
	}

	public int getErfNumber() {
		return erfNumber;
	}
	
	/**
	 * this is the toString that will print out the info from the project class
	 */
	public String toString() {
		String objectString = "\nProject number: " + projectNumber +
			"\nProject name: " + projectName +
			"\nBuilding type: " + buildingType +
			"\nPhysical Address: " + physicalAddress +
			"\nERF number: " + erfNumber +
			"\nAmount due: R " + amountDue +
			"\nAmount paid: R " + amountReceived +
			"\nDeadline: " + deadline + 
			"\n\n******   Consumer   *******" +
			"\n\n" + person + "\n" +
			"\n\n******   Architect   *******" +
			"\n\n" + person2 + "\n" +
			"\n\n******   Contractor   *******" +
			"\n\n" + person3 + "\n";
		
		return objectString;
}

}
