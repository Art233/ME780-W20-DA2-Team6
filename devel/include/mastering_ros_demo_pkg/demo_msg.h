// Generated by gencpp from file mastering_ros_demo_pkg/demo_msg.msg
// DO NOT EDIT!


#ifndef MASTERING_ROS_DEMO_PKG_MESSAGE_DEMO_MSG_H
#define MASTERING_ROS_DEMO_PKG_MESSAGE_DEMO_MSG_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mastering_ros_demo_pkg
{
template <class ContainerAllocator>
struct demo_msg_
{
  typedef demo_msg_<ContainerAllocator> Type;

  demo_msg_()
    : number(0.0)  {
    }
  demo_msg_(const ContainerAllocator& _alloc)
    : number(0.0)  {
  (void)_alloc;
    }



   typedef float _number_type;
  _number_type number;





  typedef boost::shared_ptr< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> const> ConstPtr;

}; // struct demo_msg_

typedef ::mastering_ros_demo_pkg::demo_msg_<std::allocator<void> > demo_msg;

typedef boost::shared_ptr< ::mastering_ros_demo_pkg::demo_msg > demo_msgPtr;
typedef boost::shared_ptr< ::mastering_ros_demo_pkg::demo_msg const> demo_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mastering_ros_demo_pkg

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'mastering_ros_demo_pkg': ['/home/art233/catkin_ws/src/mastering_ros_demo_pkg/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ded049c24c756963282afab14b2d0f6d";
  }

  static const char* value(const ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xded049c24c756963ULL;
  static const uint64_t static_value2 = 0x282afab14b2d0f6dULL;
};

template<class ContainerAllocator>
struct DataType< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mastering_ros_demo_pkg/demo_msg";
  }

  static const char* value(const ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 number\n"
;
  }

  static const char* value(const ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.number);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct demo_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mastering_ros_demo_pkg::demo_msg_<ContainerAllocator>& v)
  {
    s << indent << "number: ";
    Printer<float>::stream(s, indent + "  ", v.number);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MASTERING_ROS_DEMO_PKG_MESSAGE_DEMO_MSG_H
