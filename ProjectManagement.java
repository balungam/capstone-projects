package capstone1;

import java.util.Scanner;

//This is the main class to test all the objects and to finalise the project

public class ProjectManagement {
	public static void main(String[] args) {
		
		//I created the scanner "input" to take in inputs from te user.
		
		Scanner input = new Scanner(System.in);
		
		//I created a new Consumer using the Consumer object
		Consumer balunga = new Consumer("Balunga Mbolekwa", "0123567788", "balungam@yahoo.com", "52 Tlale Street", 0.0);
		
		//I created a new Architect using the Architect object
		Architect vuyo = new Architect ("Vuyo Maake", "0123567899", "vuyo@tse.co.za", "89 Maar street" );
		
		//I created a new Contractor using the Contractor object
		Contractor bstConstruction = new Contractor ("bstConstruction", "0127378899", "info@bstconstruction.co.za","1025 Pretoria road");
		
		/**
		 * I asked the user for the following inputs
		 * the following inputs are used to create the new project
		 * i asked the user to input:
		 * project number, project name, building type, address,
		 * ERF number, deadline and the quotation amount.
		 */
		System.out.println("Enter the project number: ");
		int number = input.nextInt();
		input.nextLine();
		
		System.out.println("Enter the project name: ");
		String name = input.nextLine();
		
		System.out.println("Enter the building type: ");
		String type = input.nextLine();
		
		System.out.println("Enter the physical address: ");
		String address = input.nextLine();
		
		System.out.println("Enter the ERF number: ");
		int erf = input.nextInt();
		input.nextLine();
		
		System.out.println("Enter the deadline: ");
		String dueDate = input.nextLine();
		
		System.out.println("Enter the total fee being charged: ");
		float fees = input.nextFloat();
		input.nextLine();
		

		//i created the new Project using the all the inputs from the user
		Project house = new Project(number, name, type, address, erf, dueDate, fees , balunga, vuyo, bstConstruction); 
		
		System.out.println("******   Initial invoice   ******");
		System.out.println(house);
		
		/**
		 * I asked the user to input all the modifications they 
		 * want to do to the final invoice.
		 * I asked the user to input:
		 * 		the payment made by the consumer.
		 * 		the contractor's new telephone.
		 * 		the contractor's new email.
		 * and the revised deadline.
		 *  
		 */
		System.out.print("How much did the consumer pay? ");
		double payment = input.nextDouble();
		input.nextLine();
		
		System.out.print("Update the contractor's telepone: ");
		String contact1 = input.nextLine();
		
		System.out.print("Update the contractor's email: ");
		String contact2 = input.nextLine();
		
		System.out.print("Change the due date: ");
		String dueDate2 = input.nextLine();
		

		 //* I used the setamountPaid method to update the amount paid,
		 //* by the consumer.
		balunga.setAmountPaid(balunga.getAmountPaid() + payment);
		
		//I used the setAmountReceived to update the project,
		//with the amount paid by the consumer.
		house.setAmountReceived(balunga.getAmountPaid());
		
		//I used the setAmountDue to update the amount due for the project.
		house.setAmountDue(fees - balunga.getAmountPaid());
		
		//I used the setTephone and setEmail methods,
		// to update the contractor's contact details
		bstConstruction.setTelephone(contact1);
		bstConstruction.setEmail(contact2);
		
		//I used the setDeadline to update the deadline for the project
		house.setDeadline(dueDate2);
		
		/**
		 * To finalise the project i printed out the project with all the updated,
		 * information.
		 */
		System.out.println("******   Updated Invoice   ******");
		System.out.println(house);
	}	
}
