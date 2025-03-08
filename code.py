import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Upload, CheckCircle, ListOrdered, DollarSign, Gift } from "lucide-react";

export default function ReportVehicle() {
  const [submitted, setSubmitted] = useState(false);
  const [reportCount, setReportCount] = useState(0);
  const [rewards, setRewards] = useState([]);
  const [cashback, setCashback] = useState(0);
  const [showRewards, setShowRewards] = useState(false);

  const handleSubmit = () => {
    setSubmitted(true);
    const newReportCount = reportCount + 1;
    setReportCount(newReportCount);
    
    if (newReportCount % 5 === 0) {
      setCashback(cashback + 20); // Cashback reward every 5th report
      setRewards([...rewards, { type: "Cashback", amount: 20, claimed: false }]);
    } else {
      const rewardOptions = [
        "Discount Coupon",
        "Shopping Voucher",
        "Restaurant Deal",
        "No Reward This Time"
      ];
      const randomReward = rewardOptions[Math.floor(Math.random() * rewardOptions.length)];
      if (randomReward !== "No Reward This Time") {
        setRewards([...rewards, { type: randomReward, claimed: false }]);
      }
    }
  };

  const handleWithdraw = () => {
    alert(You have withdrawn ₹${cashback}!);
    setCashback(0);
  };

  const handleClaimReward = (index) => {
    const updatedRewards = [...rewards];
    updatedRewards[index].claimed = true;
    setRewards(updatedRewards);
  };

  return (
    <div className="max-w-5xl mx-auto p-6 space-y-6 flex flex-col items-center bg-gradient-to-b from-green-200 to-green-500 min-h-screen">
      <div className="flex justify-between w-full px-6">
        <div className="flex items-center gap-2 text-white text-lg font-semibold">
          <ListOrdered size={24} /> No. of Reports: {reportCount}
        </div>
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-2 text-white text-lg font-semibold cursor-pointer" onClick={() => setShowRewards(true)}>
            <Gift size={24} /> Rewards
          </div>
          <div className="flex items-center gap-2 text-white text-lg font-semibold">
            <DollarSign size={24} /> Cashback Won: ₹{cashback}
            {cashback > 0 && (
              <Button onClick={handleWithdraw} className="ml-2 bg-yellow-500 hover:bg-yellow-600 text-white text-sm font-semibold px-3 py-1 rounded-lg shadow-lg">
                Withdraw Cash
              </Button>
            )}
          </div>
        </div>
      </div>
      {!submitted ? (
        <>
          <h1 className="text-3xl font-bold text-center text-white drop-shadow-md">Report a Polluting Vehicle</h1>
          <p className="text-center text-white text-lg font-semibold">"Your small step can make a big difference! Help us create a cleaner future."</p>
          
          <Card className="p-6 space-y-6 shadow-2xl rounded-xl w-2/4 bg-white border-2 border-green-600">
            <CardContent className="space-y-4">
              <Input type="text" placeholder="Enter vehicle number" className="border-green-500" />
              <div>
                <label className="block text-sm font-semibold text-green-700">Upload Photo/Video as Proof</label>
                <Button variant="outline" className="flex items-center gap-2 bg-green-600 text-white hover:bg-green-700">
                  <Upload size={16} /> Upload File
                </Button>
              </div>
              <Input type="text" placeholder="Your Name" className="border-green-500" />
              <Input type="email" placeholder="Your Email" className="border-green-500" />
              <Input type="tel" placeholder="Your Phone Number" className="border-green-500" />
              <Textarea placeholder="Any additional details..." className="border-green-500" />
              <Button onClick={handleSubmit} className="w-full bg-green-600 hover:bg-green-700 text-white text-lg font-semibold shadow-lg">
                Submit Report
              </Button>
            </CardContent>
          </Card>
        </>
      ) : (
        <Card className="p-8 space-y-6 shadow-2xl rounded-xl bg-white border-2 border-green-600 text-center max-w-lg">
          <CheckCircle className="text-green-600 w-16 h-16 mx-auto" />
          <h2 className="text-2xl font-bold text-green-700">Thank You!</h2>
          <p className="text-lg text-gray-700">We appreciate your effort in reporting pollution. Your contribution helps make the environment cleaner and safer!</p>
          <p className="text-green-600 font-semibold">Rewards will be given soon!</p>
          <Button onClick={() => setSubmitted(false)} className="bg-green-600 hover:bg-green-700 text-white text-lg font-semibold shadow-lg">
            Report Another Vehicle
          </Button>
        </Card>
      )}
      {showRewards && (
        <Card className="p-6 shadow-2xl rounded-xl bg-white border-2 border-green-600 text-center max-w-md absolute top-20 right-10">
          <h2 className="text-2xl font-bold text-green-700">Your Rewards</h2>
          <ul className="mt-4 space-y-2">
            {rewards.length === 0 ? (
              <p className="text-gray-600">No rewards yet. Keep reporting!</p>
            ) : (
              rewards.map((reward, index) => (
                <li key={index} className="text-lg text-gray-700 flex justify-between items-center border-b pb-2">
                  {reward.type} {reward.amount ? ₹${reward.amount} : ""}
                  {!reward.claimed && (
                    <Button onClick={() => handleClaimReward(index)} className="bg-green-500 hover:bg-green-600 text-white text-sm font-semibold px-3 py-1 rounded-lg shadow-md">
                      Claim
                    </Button>
                  )}
                </li>
              ))
            )}
          </ul>
          <Button onClick={() => setShowRewards(false)} className="mt-4 bg-red-500 hover:bg-red-600 text-white text-sm font-semibold px-4 py-2 rounded-lg shadow-lg">
            Close
          </Button>
        </Card>
      )}
    </div>
  );
}
